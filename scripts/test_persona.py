#!/usr/bin/env python3
"""
龙娘小夏人设测试工具
测试人设一致性，生成台词示例
"""

import json
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class PersonaTester:
    """人设测试器"""
    
    def __init__(self, persona_path="config/persona.json"):
        self.persona_path = Path(persona_path)
        with open(self.persona_path, 'r', encoding='utf-8') as f:
            self.persona = json.load(f)
    
    def test_all(self):
        """运行所有测试"""
        self.test_basic_info()
        self.test_speech_patterns()
        self.test_comment_templates()
        self.test_emotion_responses()
        self.test_consistency()
    
    def test_basic_info(self):
        """测试基本信息"""
        console.print(Panel.fit(
            "[bold blue]🐉 龙娘小夏人设测试[/bold blue]\n"
            "基础信息验证",
            border_style="blue"
        ))
        
        identity = self.persona['identity']
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("项目")
        table.add_column("内容")
        
        table.add_row("姓名", identity.get('name', '未知'))
        table.add_row("身份", identity.get('role', '未知'))
        table.add_row("年龄", identity.get('age', '未知'))
        table.add_row("种族", identity.get('species', '未知'))
        
        console.print(table)
    
    def test_speech_patterns(self):
        """测试台词模式"""
        console.print("\n" + "="*50)
        console.print("🎤 [bold]台词测试[/bold]", style="cyan")
        print("="*50)
        
        patterns = self.persona['personality']['speech_patterns']
        
        for scene, text in patterns.items():
            console.print(f"\n[场景] {scene}")
            console.print(f"  {text}", style="yellow")
    
    def test_comment_templates(self):
        """测试评论模板"""
        console.print("\n" + "="*50)
        console.print("💬 [bold]评论模板测试[/bold]", style="cyan")
        print("="*50)
        
        templates = self.persona['interaction']['comment_templates']
        
        for template_type, text in templates.items():
            console.print(f"\n[{template_type}]")
            console.print(f"  {text}", style="green")
    
    def test_emotion_responses(self):
        """测试情绪响应"""
        console.print("\n" + "="*50)
        console.print("🎭 [bold]情绪响应测试[/bold]", style="cyan")
        print("="*50)
        
        emotions = ['happy', 'angry', 'shy', 'excited', 'sleepy']
        expressions = self.persona['visual']['expressions']
        
        for emotion in emotions:
            if emotion in expressions:
                console.print(f"\n[{emotion}]")
                console.print(f"  表情: {expressions[emotion]}", style="magenta")
    
    def test_consistency(self):
        """测试人设一致性"""
        console.print("\n" + "="*50)
        console.print("✅ [bold]人设一致性测试[/bold]", style="cyan")
        print("="*50)
        
        checks = []
        
        # 检查口头禅
        catchphrase = self.persona['personality']['catchphrase']
        if '本龙' in catchphrase or '哼' in catchphrase:
            checks.append(("口头禅", "✅", "包含'本龙'或'哼'"))
        else:
            checks.append(("口头禅", "❌", "缺少'本龙'或'哼'"))
        
        # 检查回复规则
        rules = self.persona['interaction']['response_rules']
        if len(rules) >= 5:
            checks.append(("回复规则", "✅", f"{len(rules)} 条规则"))
        else:
            checks.append(("回复规则", "❌", "规则数量不足"))
        
        # 检查敏感词
        forbidden = self.persona['forbidden']['topics']
        if len(forbidden) >= 3:
            checks.append(("敏感词", "✅", f"{len(forbidden)} 个话题"))
        else:
            checks.append(("敏感词", "❌", "话题数量不足"))
        
        # 检查内容策略
        strategy = self.persona['content_strategy']
        if 'video_types' in strategy:
            checks.append(("内容策略", "✅", f"{len(strategy['video_types'])} 种类型"))
        else:
            checks.append(("内容策略", "❌", "缺少内容策略"))
        
        # 输出检查结果
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("检查项")
        table.add_column("状态")
        table.add_column("说明")
        
        for check in checks:
            table.add_row(check[0], check[1], check[2])
        
        console.print(table)
    
    def generate_demo_conversation(self):
        """生成示例对话"""
        console.print("\n" + "="*50)
        console.print("🎬 [bold]示例对话[/bold]", style="cyan")
        print("="*50)
        
        conversation = [
            ("粉丝", "龙娘你好可爱！"),
            ("小夏", "哼，知道就好～本龙可是很厉害的！"),
            ("粉丝", "能教我用 AI 做视频吗？"),
            ("小夏", "这个问题嘛～让本龙想想...（思考）哼，本龙才不是想教你呢！"),
            ("粉丝", "谢谢龙娘！"),
            ("小夏", "哼...加油哦！本龙会看着你的...（小声）"),
        ]
        
        for speaker, text in conversation:
            if speaker == "小夏":
                console.print(f"\n[小夏] {text}", style="green")
            else:
                console.print(f"\n[粉丝] {text}", style="yellow")


def main():
    """主函数"""
    tester = PersonaTester()
    tester.test_all()
    tester.generate_demo_conversation()
    
    console.print("\n" + "="*50)
    console.print("✅ [bold]测试完成！[/bold]", style="green")
    print("="*50)


if __name__ == "__main__":
    main()
