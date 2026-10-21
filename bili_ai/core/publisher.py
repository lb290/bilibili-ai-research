"""
视频投稿与数据管理模块
负责视频上传、数据分析
"""

import json
from datetime import datetime
from pathlib import Path


class Publisher:
    """管理视频投稿和数据"""
    
    def __init__(self):
        self.uploaded_videos = []
        self.data_file = Path.home() / ".config" / "bili_ai" / "videos.json"
        self._load_data()
    
    def _load_data(self):
        """加载视频数据"""
        if self.data_file.exists():
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.uploaded_videos = json.load(f)
    
    def _save_data(self):
        """保存视频数据"""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.uploaded_videos, f, ensure_ascii=False, indent=2)
    
    def upload(self, file_path, title, tags=None, description="", source=""):
        """
        投稿视频
        实际应调用 bili-cli
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"视频文件不存在: {file_path}")
        
        print(f"📤 投稿视频:")
        print(f"   文件: {file_path}")
        print(f"   标题: {title}")
        print(f"   标签: {tags}")
        print(f"   简介: {description}")
        print(f"   来源: {source}")
        print(f"   ⚠️ 已勾选'含AI生成内容'")
        
        # 模拟投稿成功
        bv_id = f"BV{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        video_data = {
            "bv_id": bv_id,
            "title": title,
            "file": str(file_path),
            "tags": tags or [],
            "description": description,
            "source": source,
            "uploaded_at": datetime.now().isoformat(),
            "status": "published"
        }
        
        self.uploaded_videos.append(video_data)
        self._save_data()
        
        print(f"✅ 投稿成功！BV号: {bv_id}")
        
        return {"ok": True, "bv_id": bv_id}
    
    def get_video_stats(self, bv_id):
        """
        获取视频数据
        实际应调用 bili-cli
        """
        # 模拟数据
        return {
            "bv_id": bv_id,
            "views": 12345,
            "likes": 567,
            "coins": 89,
            "favorites": 234,
            "comments": 45,
            "avg_watch_time": "2:34",
            "completion_rate": 0.65,
            "published_at": "2026-10-21 12:00:00"
        }
    
    def get_account_stats(self):
        """
        获取账号数据
        实际应调用 bili-cli
        """
        # 模拟数据
        return {
            "followers": 5000,
            "following": 123,
            "total_views": 150000,
            "total_likes": 5000,
            "videos_count": 15,
            "growth_30d": {
                "followers": 500,
                "views": 20000
            }
        }
    
    def edit_video(self, bv_id, title=None, tags=None, description=None):
        """
        修改视频信息
        实际应调用 bili-cli
        """
        for video in self.uploaded_videos:
            if video["bv_id"] == bv_id:
                if title:
                    video["title"] = title
                if tags:
                    video["tags"] = tags
                if description:
                    video["description"] = description
                
                video["updated_at"] = datetime.now().isoformat()
                self._save_data()
                
                print(f"✅ 已修改视频 {bv_id}")
                return {"ok": True}
        
        raise ValueError(f"视频不存在: {bv_id}")
