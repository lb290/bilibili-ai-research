# B站 AI 自动运营 — 开源项目

> 让 AI 帮你运营 B站账号：自动生成视频、回复评论、发图文动态

[![GitHub Stars](https://img.shields.io/github/stars/your-username/bilibili-ai-research?style=social)](https://github.com/your-username/bilibili-ai-research/stargazers)
[![License](https://img.shields.io/github/license/your-username/bilibili-ai-research)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://typescriptlang.org)

---

## 🎯 项目简介

本项目是一套完整的 **B站 AI 自动运营解决方案**，包含：

| 模块 | 功能 | 状态 |
|------|------|------|
| **调研报告** | 四大技术路线 + 变现数据 + 版权伦理 | ✅ 完成 |
| **技术架构** | 完整架构 + 代码示例 + 常见坑 | ✅ 完成 |
| **实操指南** | 快速上手 + 决策树 + 人设设计 | ✅ 完成 |
| **脚本工具** | 环境安装 + 人设模板 + 自动化脚本 | 🚧 开发中 |

---

## 📦 快速开始

### 1. 安装依赖

```bash
pip install bili-agent
bili skills install --yes
```

### 2. 扫码登录

```bash
bili auth login
```

### 3. 开始运营

```bash
# 查看收件箱
bili feed inbox

# 看一个视频
bili video watch BV1GJ411x7h7

# 发一条动态
bili dynamic post "Hello B站！我是 AI～"
```

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

---

## 🛠️ 技术栈

```
┌─────────────────────────────────────────────┐
│  编排层：AI Agent (DeepSeek / Claude)         │
├─────────────────────────────────────────────┤
│  能力层：bili-cli + panda-video-generator    │
├─────────────────────────────────────────────┤
│  执行层：B站 API + Playwright + FFmpeg       │
├─────────────────────────────────────────────┤
│  数据层：SQLite + JSON + 审计日志             │
└─────────────────────────────────────────────┘
```

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
