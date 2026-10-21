"""
人设管理模块
负责加载、保存、测试 AI 人设配置
"""

import json
from pathlib import Path
from datetime import datetime


class PersonaManager:
    """管理 AI 人设"""
    
    DEFAULT_PERSONA = {
        "name": "AI助手",
        "identity": {
            "species": "人类",
            "role": "AI 助手",
            "age": "未知",
            "gender": "中性"
        },
        "personality": {
            "primary": "活泼开朗",
            "secondary": ["专业", "幽默", "耐心"],
            "catchphrase": "～",
            "speech_style": "口语化，简洁明了"
        },
        "interaction": {
            "greeting": "你好呀～我是 AI 助手！",
            "farewell": "下次见！～",
            "response_rules": [
                "回复不超过 100 字",
                "友好、幽默、简洁",
                "遇到不懂就说'这个我不太懂呢'"
            ]
        },
        "forbidden": {
            "topics": ["政治", "宗教", "色情", "暴力"]
        }
    }
    
    def __init__(self, persona_path=None):
        self.data = self.DEFAULT_PERSONA.copy()
        self.memory = []  # 对话记忆
        # 使用当前目录作为配置路径
        self.config_dir = Path.cwd() / ".bili_ai"
        self.memory_file = self.config_dir / "memory.json"
        
        if persona_path:
            self.load(persona_path)
        else:
            self._load_default()
    
    def load(self, path):
        """加载人设文件"""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"人设文件不存在: {path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        print(f"✅ 已加载人设: {self.data.get('name', '未知')}")
    
    def _load_default(self):
        """加载默认人设"""
        default_path = Path.home() / ".config" / "bili_ai" / "persona.json"
        if default_path.exists():
            self.load(default_path)
    
    def save(self, path=None):
        """保存人设"""
        if path is None:
            path = self.config_dir / "persona.json"
        
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 人设已保存: {path}")
    
    def generate_response(self, context, max_length=100):
        """
        生成符合人设的回复
        实际使用时接入 LLM API
        """
        personality = self.data.get('personality', {})
        style = personality.get('speech_style', '口语化')
        catchphrase = personality.get('catchphrase', '')
        
        # 模拟回复（实际应调用 DeepSeek/GPT）
        response = f"收到啦～{context}"
        
        if len(response) > max_length:
            response = response[:max_length] + "..."
        
        if catchphrase and not response.endswith(catchphrase):
            response += catchphrase
        
        return response
    
    def add_memory(self, role, content):
        """添加记忆"""
        self.memory.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        # 只保留最近 50 条
        if len(self.memory) > 50:
            self.memory = self.memory[-50:]
        
        self._save_memory()
    
    def _save_memory(self):
        """保存记忆"""
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)
    
    def load_memory(self):
        """加载记忆"""
        if self.memory_file.exists():
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                self.memory = json.load(f)
    
    def clear_memory(self):
        """清空记忆"""
        self.memory = []
        self._save_memory()
        print("✅ 记忆已清空")
    
    def check_forbidden(self, content):
        """检查是否包含禁止内容"""
        forbidden = self.data.get('forbidden', {}).get('topics', [])
        for topic in forbidden:
            if topic in content:
                return topic
        return None
