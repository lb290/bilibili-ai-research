"""
B站 AI 自动运营 - CLI 入口
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

from .core.persona import PersonaManager
from .core.interactor import Interactor
from .core.publisher import Publisher
from .core.video_generator import VideoGenerator

console = Console()


def main():
    """主入口"""
    parser = argparse.ArgumentParser(
        prog="bili-ai",
        description="🚀 B站 AI 自动运营工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📚 示例:
  bili-ai inbox                    查看收件箱
  bili-ai reply 123 "谢谢"         回复评论
  bili-ai post "动态内容"           发动态
  bili-ai persona --show           显示人设
  bili-ai stats --account          查看账号数据
  bili-ai demo                     运行演示

📖 文档: https://github.com/lb290/bilibili-ai-research
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # 收件箱
    p_inbox = subparsers.add_parser("inbox", help="查看收件箱")
    p_inbox.add_argument("--unreplied", action="store_true", help="只显示未回复")
    
    # 回复
    p_reply = subparsers.add_parser("reply", help="回复评论")
    p_reply.add_argument("comment_id", help="评论 ID")
    p_reply.add_argument("content", help="回复内容")
    p_reply.add_argument("--bv", help="视频 BV 号")
    p_reply.add_argument("--at", action="store_true", help="@ 用户")
    
    # 发动态
    p_post = subparsers.add_parser("post", help="发动态")
    p_post.add_argument("content", help="动态内容")
    p_post.add_argument("--images", nargs="+", help="图片路径")
    
    # 人设
    p_persona = subparsers.add_parser("persona", help="人设管理")
    p_persona.add_argument("--load", help="加载人设文件")
    p_persona.add_argument("--show", action="store_true", help="显示当前人设")
    p_persona.add_argument("--test", help="测试回复")
    
    # 数据
    p_stats = subparsers.add_parser("stats", help="查看数据")
    p_stats.add_argument("--bv", help="视频 BV 号")
    p_stats.add_argument("--account", action="store_true", help="账号数据")
    
    # 生成视频
    p_generate = subparsers.add_parser("generate", help="生成视频")
    p_generate.add_argument("--script", help="脚本文件")
    p_generate.add_argument("--text", help="文本内容")
    p_generate.add_argument("--output", default="output.mp4", help="输出文件")
    
    # 投稿
    p_upload = subparsers.add_parser("upload", help="投稿视频")
    p_upload.add_argument("--file", required=True, help="视频文件")
    p_upload.add_argument("--title", required=True, help="标题")
    p_upload.add_argument("--tags", help="标签（逗号分隔）")
    p_upload.add_argument("--desc", help="简介")
    
    # Demo
    subparsers.add_parser("demo", help="运行演示")
    
    # Setup
    subparsers.add_parser("setup", help="初始化配置")
    
    args = parser.parse_args()
    
    if not args.command:
        print_welcome()
        parser.print_help()
        return
    
    try:
        handle_command(args)
    except KeyboardInterrupt:
        console.print("\n👋 已取消", style="yellow")
    except Exception as e:
        console.print(f"❌ 错误: {e}", style="red")
        sys.exit(1)


def handle_command(args):
    """处理命令"""
    if args.command == "inbox":
        cmd_inbox(args)
    elif args.command == "reply":
        cmd_reply(args)
    elif args.command == "post":
        cmd_post(args)
    elif args.command == "persona":
        cmd_persona(args)
    elif args.command == "stats":
        cmd_stats(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "upload":
        cmd_upload(args)
    elif args.command == "demo":
        cmd_demo()
    elif args.command == "setup":
        cmd_setup()


def print_welcome():
    """打印欢迎信息"""
    console.print(Panel.fit(
        "[bold blue]🚀 B站 AI 自动运营工具[/bold blue]\n"
        "让 AI 帮你运营 B站账号",
        border_style="blue"
    ))


def cmd_inbox(args):
    """查看收件箱"""
    console.print("📬 [bold]收件箱[/bold]", style="cyan")
    
    interactor = Interactor()
    inbox = interactor.check_inbox(unreplied=args.unreplied)
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("类型", style="dim")
    table.add_column("来自")
    table.add_column("内容")
    table.add_column("时间")
    
    for item in inbox:
        table.add_row(
            item["type"],
            item["from"],
            item["content"][:30] + "..." if len(item["content"]) > 30 else item["content"],
            item["time"]
        )
    
    console.print(table)


def cmd_reply(args):
    """回复评论"""
    console.print(f"💬 [bold]回复评论[/bold] {args.comment_id}", style="cyan")
    
    interactor = Interactor()
    result = interactor.reply(
        bv_id=args.bv or "unknown",
        comment_id=args.comment_id,
        content=args.content,
        at=args.at
    )
    
    console.print(f"✅ {result['message']}", style="green")


def cmd_post(args):
    """发动态"""
    console.print("📝 [bold]发布动态[/bold]", style="cyan")
    
    interactor = Interactor()
    result = interactor.post_dynamic(args.content, args.images)
    
    console.print(f"✅ {result['message']}", style="green")


def cmd_persona(args):
    """人设管理"""
    persona = PersonaManager()
    
    if args.load:
        persona.load(args.load)
        console.print(f"✅ 已加载人设: {persona.data.get('name', '未知')}", style="green")
    elif args.show:
        console.print(json.dumps(persona.data, ensure_ascii=False, indent=2))
    elif args.test:
        response = persona.generate_response(args.test)
        console.print(f"💬 [bold]测试回复:[/bold] {response}")
    else:
        console.print(f"👤 当前人设: {persona.data.get('name', '未知')}")
        console.print(f"   性格: {persona.data.get('personality', {}).get('primary', '未知')}")


def cmd_stats(args):
    """查看数据"""
    publisher = Publisher()
    
    if args.bv:
        stats = publisher.get_video_stats(args.bv)
        console.print(f"📊 [bold]视频数据[/bold] {args.bv}", style="cyan")
        for key, value in stats.items():
            console.print(f"  {key}: {value}")
    elif args.account:
        stats = publisher.get_account_stats()
        console.print("📈 [bold]账号数据[/bold]", style="cyan")
        for key, value in stats.items():
            console.print(f"  {key}: {value}")


def cmd_generate(args):
    """生成视频"""
    generator = VideoGenerator()
    
    if args.script:
        result = generator.generate(args.script, args.output)
    elif args.text:
        result = generator.generate_from_text(args.text, args.output)
    else:
        console.print("❌ 请提供 --script 或 --text", style="red")
        return
    
    console.print(f"✅ 视频已生成: {result['output']}", style="green")


def cmd_upload(args):
    """投稿视频"""
    publisher = Publisher()
    
    tags = args.tags.split(",") if args.tags else []
    result = publisher.upload(
        file_path=args.file,
        title=args.title,
        tags=tags,
        description=args.desc
    )
    
    console.print(f"✅ 投稿成功！BV号: {result['bv_id']}", style="green")


def cmd_demo():
    """运行演示"""
    from examples.demo import main as demo_main
    demo_main()


def cmd_setup():
    """初始化配置"""
    config_dir = Path.home() / ".config" / "bili_ai"
    config_dir.mkdir(parents=True, exist_ok=True)
    
    console.print("🔧 [bold]初始化配置[/bold]", style="cyan")
    
    # 创建默认人设
    persona_path = config_dir / "persona.json"
    if not persona_path.exists():
        persona = PersonaManager()
        persona.save(persona_path)
        console.print(f"✅ 已创建默认人设: {persona_path}")
    
    # 创建 .env
    env_path = config_dir / ".env"
    if not env_path.exists():
        env_path.write_text("DEEPSEEK_API_KEY=your-api-key\n")
        console.print(f"✅ 已创建环境变量模板: {env_path}")
    
    console.print("✅ 配置完成！", style="green")


if __name__ == "__main__":
    main()
