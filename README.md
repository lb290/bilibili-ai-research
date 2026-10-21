# B站 AI 自动运营 — 开源项目

> 让 AI 帮你运营 B站账号：自动生成视频、回复评论、发图文动态

[![GitHub Stars](https://img.shields.io/github/stars/lb290/bilibili-ai-research?style=social)](https://github.com/lb290/bilibili-ai-research/stargazers)
[![License](https://img.shields.io/github/license/lb290/bilibili-ai-research)](https://github.com/lb290/bilibili-ai-research/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)

---

## 🎯 项目简介

本项目是一套完整的 **B站 AI 自动运营解决方案**，包含：

| 模块 | 功能 | 状态 |
|------|------|------|
| **调研报告** | 四大技术路线 + 变现数据 + 版权伦理 | ✅ 完成 |
| **技术架构** | 完整架构 + 代码示例 + 常见坑 | ✅ 完成 |
| **实操指南** | 快速上手 + 决策树 + 人设设计 | ✅ 完成 |
| **Python 工具** | CLI 工具 + 核心模块 + 可运行代码 | ✅ 完成 |
| **Demo 演示** | 完整功能演示，开箱即用 | ✅ 完成 |
| **预设人设** | 龙娘小夏 — 傲娇龙娘 UP 主 | ✅ 完成 |

---

## 🚀 快速开始

### 5 分钟上手

```bash
# 1. 克隆项目
git clone https://github.com/lb290/bilibili-ai-research.git
cd bilibili-ai-research

# 2. 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 3. 安装依赖
pip install rich pydantic python-dotenv aiohttp httpx openai edge-tts

# 4. 测试人设
python scripts/test_persona.py

# 5. 运行演示
python -c "from bili_ai.cli import main; main()" demo
```

### 详细步骤

👉 查看 [快速开始指南](./docs/快速开始.md)

---

## 🐉 预设人设：龙娘小夏

**傲娇龙娘 UP 主**，已配置完整台词和视觉形象。

```
口头禅：哼，本龙才不是帮你呢！
性格：傲娇 + 腹黑 + 温柔 + 活泼
```

**测试结果**：
```
✅ 口头禅：包含"本龙"和"哼"
✅ 回复规则：7 条规则
✅ 敏感词：4 个话题
✅ 内容策略：4 种类型
```

**示例对话**：
```
[粉丝] 龙娘你好可爱！
[小夏] 哼，知道就好～本龙可是很厉害的！

[粉丝] 能教我用 AI 做视频吗？
[小夏] 这个问题嘛～让本龙想想...（思考）哼，本龙才不是想教你呢！
```

**完整文档**：[龙娘小夏人设设定](./docs/龙娘小夏人设设定.md)

---

## 📚 文档目录

| 文档 | 内容 | 适合人群 |
|------|------|---------|
| [01_调研总览.md](./01_调研总览.md) | 四大技术路线 + 变现数据 + 版权伦理 | 所有读者 |
| [02_技术架构详解.md](./02_技术架构详解.md) | 技术架构 + 代码示例 + 常见坑 | 开发者 |
| [03_实操指南.md](./03_实操指南.md) | 快速上手 + 决策树 + 人设设计 | 实操者 |
| [04_快速参考.md](./04_快速参考.md) | 命令速查 + 成本估算 | 快速查阅 |
| [05_爆款案例分析.md](./05_爆款案例分析.md) | BV1pinc6FEjR 案例深度拆解 | 运营者 |
| [06_版权与伦理.md](./06_版权与伦理.md) | 中国 AI 法规 + 合规清单 | 所有人 |
| [07_项目交接.md](./07_项目交接.md) | 新会话衔接指南 | 继续工作 |
| [龙娘小夏人设设定.md](./docs/龙娘小夏人设设定.md) | 完整人设文档 | 运营者 |
| [动漫女性角色调研.md](./docs/动漫女性角色调研.md) | 人气角色分析 | 人设设计 |
| [发布流程.md](./docs/发布流程.md) | 发布检查清单 | 运营者 |
| [30天运营计划.md](./docs/30天运营计划.md) | 详细运营计划 | 运营者 |
| [快速开始.md](./docs/快速开始.md) | 5 分钟快速开始 | 新手 |

---

## 🛠️ 核心功能

### 1. 人设管理

```bash
# 查看人设
bili-ai persona --show

# 测试回复
bili-ai persona --test "这个视频做得真好！"

# 加载新人设
bili-ai persona --load config/my_persona.json
```

### 2. 互动管理

```bash
# 查看收件箱
bili-ai inbox

# 回复评论
bili-ai reply 12345 "谢谢支持！～" --at

# 发动态
bili-ai post "新视频发布啦！"
```

### 3. 数据监控

```bash
# 查看视频数据
bili-ai stats --bv BVxxxxx

# 查看账号数据
bili-ai stats --account
```

### 4. 视频生成

```bash
# 从脚本生成视频
python -m bili_ai generate --script output/video_script.json

# 从文本生成视频
python -m bili_ai generate --text "大家好，今天聊聊 AI..."
```

---

## 📊 项目统计

| 指标 | 数量 |
|------|------|
| 调研文档 | 11 份 |
| Python 代码 | 805 行 |
| 人设配置 | 1 套（龙娘小夏） |
| 视频脚本 | 1 个（Day 0） |
| Git 提交 | 8 次 |

---

## ⚠️ 重要提醒

1. **用老号**：新号风控严，老号信任度高
2. **标注 AI 内容**：中国法规要求
3. **控制频率**：AI 操作节奏不超过真人
4. **保留记录**：版权证据

---

## 🤝 贡献

欢迎 Issue 和 PR！

---

## 📄 许可证

[MIT License](./LICENSE)

---

> ⚠️ 免责声明：本项目仅供学习研究，使用产生的后果由使用者自行承担。请遵守 B站用户协议与社区规则。
