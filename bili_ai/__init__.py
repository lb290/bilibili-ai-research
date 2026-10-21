#!/usr/bin/env python3
"""
B站 AI 自动运营核心模块
用法: python -m bili_ai --help
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# 导入子模块
from .core.persona import PersonaManager
from .core.publisher import Publisher
from .core.interactor import Interactor
from .core.video_generator import VideoGenerator

__version__ = "1.0.0"


def main():
    parser = argparse.ArgumentParser(
        description="B站 AI 自动运营工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 查看收件箱
  python -m bili_ai inbox

  # 回复评论
  python -m bili_ai reply --bv BVxxxxx --content "谢谢支持"

  # 发动态
  python -m bili_ai post "今天有什么新鲜事"

  # 生成视频
  python -m bili_ai generate --script scripts/script.json

  # 投稿视频
  python -m bili_ai upload --file output.mp4 --title "我的视频"
"""
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # 收件箱命令
    inbox_parser = subparsers.add_parser("inbox", help="查看收件箱")
    inbox_parser.add_argument("--unreplied", action="store_true", help="只显示未回复的评论")
    
    # 回复命令
    reply_parser = subparsers.add_parser("reply", help="回复评论")
    reply_parser.add_argument("--bv", required=True, help="视频 BV 号")
    reply_parser.add_argument("--comment-id", required=True, help="评论 ID")
    reply_parser.add_argument("--content", required=True, help="回复内容")
    reply_parser.add_argument("--at", action="store_true", help="@ 用户")
    
    # 发动态命令
    post_parser = subparsers.add_parser("post", help="发动态")
    post_parser.add_argument("content", help="动态内容")
    post_parser.add_argument("--images", nargs="+", help="图片路径")
    
    # 生成视频命令
    gen_parser = subparsers.add_parser("generate", help="生成视频")
    gen_parser.add_argument("--script", required=True, help="脚本文件路径")
    gen_parser.add_argument("--output", default="output.mp4", help="输出文件")
    
    # 投稿命令
    upload_parser = subparsers.add_parser("upload", help="投稿视频")
    upload_parser.add_argument("--file", required=True, help="视频文件")
    upload_parser.add_argument("--title", required=True, help="标题")
    upload_parser.add_argument("--tags", help="标签（逗号分隔）")
    upload_parser.add_argument("--desc", help="简介")
    upload_parser.add_argument("--source", help="来源 URL")
    
    # 人设管理命令
    persona_parser = subparsers.add_parser("persona", help="人设管理")
    persona_parser.add_argument("--load", help="加载人设文件")
    persona_parser.add_argument("--show", action="store_true", help="显示当前人设")
    persona_parser.add_argument("--test", help="测试人设回复")
    
    # 数据分析命令
    stats_parser = subparsers.add_parser("stats", help="查看数据")
    stats_parser.add_argument("--bv", help="视频 BV 号")
    stats_parser.add_argument("--account", action="store_true", help="账号数据")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # 执行命令
    try:
        handle_command(args)
    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)


def handle_command(args):
    """处理命令"""
    config_path = Path.home() / ".config" / "bili_ai"
    config_path.mkdir(parents=True, exist_ok=True)
    
    if args.command == "inbox":
        interactor = Interactor()
        interactor.check_inbox(unreplied=args.unreplied)
    
    elif args.command == "reply":
        interactor = Interactor()
        interactor.reply(
            bv_id=args.bv,
            comment_id=args.comment_id,
            content=args.content,
            at=args.at
        )
    
    elif args.command == "post":
        interactor = Interactor()
        interactor.post_dynamic(args.content, images=args.images)
    
    elif args.command == "generate":
        generator = VideoGenerator()
        generator.generate(args.script, args.output)
    
    elif args.command == "upload":
        publisher = Publisher()
        tags = args.tags.split(",") if args.tags else []
        publisher.upload(
            file_path=args.file,
            title=args.title,
            tags=tags,
            description=args.desc,
            source=args.source
        )
    
    elif args.command == "persona":
        persona = PersonaManager()
        if args.load:
            persona.load(args.load)
            print(f"✅ 人设已加载: {persona.data.get('name', '未知')}")
        elif args.show:
            print(json.dumps(persona.data, ensure_ascii=False, indent=2))
        elif args.test:
            response = persona.generate_response(args.test)
            print(f"回复: {response}")
    
    elif args.command == "stats":
        publisher = Publisher()
        if args.bv:
            stats = publisher.get_video_stats(args.bv)
            print(json.dumps(stats, ensure_ascii=False, indent=2))
        elif args.account:
            stats = publisher.get_account_stats()
            print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
