#!/bin/bash
# B站 AI 运营环境安装脚本
# 用法: bash setup.sh

set -e

echo "🚀 B站 AI 运营环境安装..."
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装 Python 3.10+"
    exit 1
fi

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js 未安装，部分功能将不可用"
    echo "   如需视频生成功能，请安装 Node.js 20+: https://nodejs.org"
fi

# 安装 bili-cli
echo "📦 安装 bili-cli..."
pip install bili-agent

# 安装技能
echo "🔧 安装 Agent 技能..."
bili skills install --yes

# 检查 ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg 未安装，视频处理功能将受限"
    echo "   安装方法:"
    echo "   - macOS: brew install ffmpeg"
    echo "   - Ubuntu: sudo apt install ffmpeg"
    echo "   - Windows: choco install ffmpeg"
fi

echo ""
echo "✅ 安装完成！"
echo ""
echo "下一步："
echo "  1. 扫码登录: bili auth login"
echo "  2. 查看文档: cat 03_实操指南.md"
echo "  3. 快速开始: cat 04_快速参考.md"
