#!/bin/bash
# 一键创建 GitHub 仓库并推送
# 用法: bash scripts/create_and_push.sh

set -e

echo "🚀 创建 GitHub 仓库..."
echo ""

# 检查 gh CLI
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    echo "✅ 使用 gh CLI 创建仓库"
    gh repo create bilibili-ai-research --public --description "B站 AI 自动运营完整解决方案" --source=.
else
    echo "⚠️  gh CLI 未安装或未登录"
    echo ""
    echo "请手动创建仓库："
    echo "  1. 打开 https://github.com/new"
    echo "  2. 仓库名: bilibili-ai-research"
    echo "  3. 选择 Public"
    echo "  4. 不要勾选 README / .gitignore"
    echo "  5. 点击 Create repository"
    echo ""
    echo "创建后运行："
    echo "  git push -u origin main"
    exit 1
fi

echo ""
echo "📤 推送代码..."
git push -u origin main

echo ""
echo "✅ 完成！仓库地址: https://github.com/lb290/bilibili-ai-research"
