#!/usr/bin/env python3
"""
使用示例
演示 B站 AI 自动运营核心功能
"""

import json
from pathlib import Path

# 导入核心模块
from bili_ai.core import PersonaManager, Interactor, Publisher, VideoGenerator


def demo_persona():
    """演示人设管理"""
    print("\n" + "="*50)
    print("🎭 人设管理演示")
    print("="*50)
    
    # 创建人设管理器
    persona = PersonaManager()
    
    # 显示人设
    print("\n当前人设:")
    print(f"  名字: {persona.data['name']}")
    print(f"  性格: {persona.data['personality']['primary']}")
    print(f"  口头禅: {persona.data['personality']['catchphrase']}")
    
    # 生成回复
    context = "这个视频做得真好！"
    response = persona.generate_response(context)
    print(f"\n回复示例:")
    print(f"  输入: {context}")
    print(f"  输出: {response}")
    
    # 检查敏感词
    test_content = "今天聊聊政治话题"
    forbidden = persona.check_forbidden(test_content)
    print(f"\n敏感词检查:")
    print(f"  内容: {test_content}")
    print(f"  结果: {'❌ 包含敏感词' if forbidden else '✅ 安全'}")


def demo_interactor():
    """演示互动管理"""
    print("\n" + "="*50)
    print("💬 互动管理演示")
    print("="*50)
    
    interactor = Interactor()
    
    # 查看收件箱
    print("\n📬 收件箱:")
    interactor.check_inbox()
    
    # 回复评论
    print("\n📝 回复评论:")
    result = interactor.reply(
        bv_id="BV1GJ411x7h7",
        comment_id="123456",
        content="谢谢支持！我会继续努力的～",
        at=True
    )
    print(f"  结果: {result['message']}")
    
    # 发动态
    print("\n📤 发布动态:")
    result = interactor.post_dynamic(
        content="新视频发布啦！大家来看看～",
        images=None
    )
    print(f"  结果: {result['message']}")


def demo_publisher():
    """演示投稿与数据"""
    print("\n" + "="*50)
    print("📤 投稿管理演示")
    print("="*50)
    
    publisher = Publisher()
    
    # 投稿视频
    print("\n📤 投稿视频:")
    result = publisher.upload(
        file_path="output/demo.mp4",
        title="AI 如何改变我们的生活",
        tags=["AI", "科技", "科普"],
        description="本视频由 AI 辅助生成",
        source="https://example.com"
    )
    print(f"  BV号: {result['bv_id']}")
    
    # 获取视频数据
    print("\n📊 视频数据:")
    stats = publisher.get_video_stats(result['bv_id'])
    print(f"  播放量: {stats['views']:,}")
    print(f"  点赞: {stats['likes']:,}")
    print(f"  完播率: {stats['completion_rate']*100:.1f}%")
    
    # 获取账号数据
    print("\n📈 账号数据:")
    account_stats = publisher.get_account_stats()
    print(f"  粉丝数: {account_stats['followers']:,}")
    print(f"  总播放: {account_stats['total_views']:,}")
    print(f"  30天涨粉: {account_stats['growth_30d']['followers']:,}")


def demo_video_generator():
    """演示视频生成"""
    print("\n" + "="*50)
    print("🎬 视频生成演示")
    print("="*50)
    
    generator = VideoGenerator()
    
    # 创建脚本
    print("\n📝 创建脚本:")
    script = generator.create_script(
        title="AI 入门教程",
        content="大家好，今天我们来聊聊 AI 是什么。AI 是人工智能的简称...",
        output_path="output/script.json"
    )
    print(f"  脚本时长: {script['duration']} 秒")
    
    # 生成视频
    print("\n🎬 生成视频:")
    result = generator.generate(
        script_path="output/script.json",
        output_path="output/demo.mp4"
    )
    print(f"  输出文件: {result['output']}")
    print(f"  视频时长: {result['duration']} 秒")


def main():
    """主函数"""
    print("\n" + "🚀"*25)
    print("B站 AI 自动运营 - 功能演示")
    print("🚀"*25)
    
    # 运行所有演示
    demo_persona()
    demo_interactor()
    demo_publisher()
    demo_video_generator()
    
    print("\n" + "="*50)
    print("✅ 演示完成！")
    print("="*50)
    print("\n下一步:")
    print("  1. 安装依赖: pip install -r requirements.txt")
    print("  2. 配置人设: 编辑 config/persona.json")
    print("  3. 开始运营: python -m bili_ai inbox")


if __name__ == "__main__":
    main()
