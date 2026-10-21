#!/usr/bin/env python3
"""
B站 AI 自动运营核心模块
"""

from .core.persona import PersonaManager
from .core.interactor import Interactor
from .core.publisher import Publisher
from .core.video_generator import VideoGenerator
from .cli import main

__version__ = "1.0.0"
__all__ = [
    'PersonaManager',
    'Interactor',
    'Publisher',
    'VideoGenerator',
    'main'
]
