"""
互动管理模块
负责评论回复、私信、动态发布
"""

import json
import time
from datetime import datetime
from pathlib import Path


class Interactor:
    """管理 B站互动"""
    
    def __init__(self):
        self.rate_limits = {
            "comment": {"interval": 10, "last": 0},
            "dm": {"interval": 10, "last": 0},
            "dynamic": {"interval": 60, "last": 0}
        }
        self.audit_log = Path.home() / ".config" / "bili_ai" / "audit.log"
        
    def check_inbox(self, unreplied=False):
        """
        查看收件箱
        实际应调用 bili-cli 或 B站 API
        """
        print("📬 收件箱:")
        print("-" * 50)
        
        # 模拟数据
        inbox = [
            {"type": "comment", "from": "用户A", "content": "视频不错！", "time": "10分钟前"},
            {"type": "mention", "from": "用户B", "content": "@你 来看看这个", "time": "30分钟前"},
            {"type": "like", "from": "用户C", "content": "赞了你的视频", "time": "1小时前"},
        ]
        
        for item in inbox:
            if unreplied and item["type"] == "comment":
                continue
            print(f"[{item['type']}] {item['from']}: {item['content']} ({item['time']})")
        
        return inbox
    
    def reply(self, bv_id, comment_id, content, at=False):
        """
        回复评论
        实际应调用 bili-cli
        """
        # 检查限流
        self._check_rate_limit("comment")
        
        # 模拟回复
        print(f"💬 回复评论 {comment_id}:")
        print(f"   BV: {bv_id}")
        print(f"   内容: {content}")
        print(f"   @: {at}")
        
        # 记录日志
        self._log("reply", {"bv": bv_id, "comment_id": comment_id, "content": content})
        
        return {"ok": True, "message": "回复成功"}
    
    def post_dynamic(self, content, images=None):
        """
        发动态
        实际应调用 bili-cli
        """
        self._check_rate_limit("dynamic")
        
        print(f"📝 发布动态:")
        print(f"   内容: {content}")
        if images:
            print(f"   图片: {len(images)} 张")
        
        self._log("dynamic", {"content": content, "images": images})
        
        return {"ok": True, "message": "发布成功"}
    
    def send_dm(self, user_id, content):
        """
        发私信
        实际应调用 bili-cli
        """
        self._check_rate_limit("dm")
        
        print(f"📩 发送私信给 {user_id}:")
        print(f"   内容: {content}")
        
        self._log("dm", {"user_id": user_id, "content": content})
        
        return {"ok": True, "message": "发送成功"}
    
    def _check_rate_limit(self, action):
        """检查限流"""
        limit = self.rate_limits.get(action, {"interval": 10, "last": 0})
        elapsed = time.time() - limit["last"]
        
        if elapsed < limit["interval"]:
            wait = limit["interval"] - elapsed
            print(f"⏳ 限流中，等待 {wait:.1f} 秒...")
            time.sleep(wait)
        
        limit["last"] = time.time()
    
    def _log(self, action, data):
        """记录审计日志"""
        self.audit_log.parent.mkdir(parents=True, exist_ok=True)
        
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "data": data
        }
        
        with open(self.audit_log, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
