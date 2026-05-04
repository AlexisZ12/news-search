<div align="center">

# News Search

一个简洁高效的命令行工具，用于通过 TianAPI 按分类和关键词搜索新闻资讯 📰

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-brightgreen?logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.x-green)](https://docs.python-requests.org/)
[![TianAPI](https://img.shields.io/badge/TianAPI-AllNews-orange)](https://www.tianapi.com/)

简体中文 | [**English**](README_EN.md)

</div>

---

## ✨ 功能特性

- 🔍 **分类搜索** - 支持 26 种新闻分类，覆盖科技、财经、体育、军事等领域
- 🎯 **关键词检索** - 精准匹配包含指定关键词的新闻文章
- 📊 **结果可调** - 灵活控制返回数量，最多支持 50 条
- 🖥️ **命令行友好** - 简洁的参数设计，易于集成和自动化
- 🌐 **数据丰富** - 返回标题、摘要、发布时间、来源、封面图等完整信息

---

## 🚀 快速开始

### 📦 安装依赖

```bash
pip install requests
```

### 🔑 获取 API Key

1. 访问 [TianAPI](https://www.tianapi.com/) 注册账号（免费）
2. 进入控制台获取 API Key
3. 设置环境变量：

```bash
export TIAN_API_KEY="your_api_key"
```

> 💡 建议将上述命令添加到 `~/.zshrc` 或 `~/.bashrc` 以实现持久化

### 🎮 基本用法

```bash
# 查看帮助 👀
python scripts/news_search.py --help

# 搜索 AI 相关新闻 🔍
python scripts/news_search.py -c ai -k "深度学习"

# 搜索国内经济新闻，返回 20 条 📈
python scripts/news_search.py -c guonei -k "经济" -n 20
```

---

## 📖 使用指南

### 🔧 参数说明

| 参数 | 缩写 | 必填 | 默认值 | 说明 |
|:----:|:----:|:----:|:------:|------|
| `--col` | `-c` | ✅ | — | 新闻分类，支持 nameid 或数字 colid |
| `--keyword` | `-k` | ✅ | — | 搜索关键词，支持多词组合 |
| `--num` | `-n` | ❌ | 10 | 返回结果数量，范围 1–50 |

### 💡 使用示例

```bash
# 🤖 AI 领域搜索
python scripts/news_search.py -c ai -k "大模型"

# 📱 科技资讯搜索
python scripts/news_search.py -c keji -k "芯片" -n 20

# 🏀 体育新闻搜索
python scripts/news_search.py -c nba -k "季后赛"

# 💰 财经新闻搜索
python scripts/news_search.py -c caijing -k "新能源"

# 🔢 使用数字 colid（科技=13）
python scripts/news_search.py -c 13 -k "人工智能"
```

---

## 📂 支持分类

| nameid | 中文名 | colid |
|:------:|:------:|:-----:|
| `social` | 社会新闻 | 5 |
| `guonei` | 国内新闻 | 7 |
| `world` | 国际新闻 | 8 |
| `huabian` | 娱乐新闻 | 10 |
| `tiyu` | 体育新闻 | 12 |
| `keji` | 科技新闻 | 13 |
| `health` | 健康知识 | 17 |
| `travel` | 旅游资讯 | 18 |
| `apple` | 苹果新闻 | 19 |
| `nba` | NBA新闻 | 20 |
| `vr` | VR科技 | 21 |
| `it` | IT资讯 | 22 |
| `football` | 足球新闻 | 26 |
| `military` | 军事新闻 | 27 |
| `ai` | 人工智能 | 29 |
| `cba` | CBA新闻 | 30 |
| `game` | 游戏资讯 | 31 |
| `caijing` | 财经新闻 | 32 |
| `dongman` | 动漫资讯 | 33 |
| `internet` | 互联网资讯 | 34 |
| `auto` | 汽车新闻 | 35 |
| `sicprobe` | 科学探索 | 36 |
| `film` | 影视资讯 | 40 |
| `huanbao` | 环保资讯 | 41 |
| `lajifenleinews` | 垃圾分类新闻 | 42 |
| `woman` | 女性新闻 | 43 |
| `nongye` | 农业新闻 | 44 |
| `esports` | 电竞资讯 | 45 |
| `petnews` | 新浪宠物 | 46 |

---

## 📊 输出示例

```
国产大模型密集发布，AI应用加速落地
近日，多家科技企业相继发布自研大语言模型，覆盖对话、编程、文生图等
多个场景，标志着国内AI产业进入加速应用阶段。
2026-05-04 09:30:00
来源：科技日报
https://example.com/news/12345
```

返回的每条新闻包含以下字段：

| 字段 | 说明 |
|:----:|------|
| `title` | 文章标题 |
| `description` | 文章摘要 |
| `ctime` | 发布时间 |
| `url` | 文章链接 |
| `picUrl` | 封面图片 URL |
| `source` | 新闻来源 |

---

## 🛠️ API 接口

本工具调用 TianAPI AllNews 接口：

```
POST https://apis.tianapi.com/allnews/index
Content-Type: application/x-www-form-urlencoded

key=<API_KEY>&col=<colid>&word=<keyword>&num=<1-50>
```

### 错误码

| 状态码 | 含义 |
|:------:|------|
| 200 | 请求成功 |
| 10001 | API Key 无效 |
| 10002 | 积分不足 |
| 10003 | API 已过期或被禁用 |
| 10004 | 请求频率超限 |

---

## 📁 项目结构

```
news-search/
├── README.md
├── SKILL.md
└── scripts/
    └── news_search.py
```

---

## ⚠️ 注意事项

> 📌 **API 限制**：免费账户每日有请求次数限制，请合理使用

> 🔑 **密钥安全**：请勿在代码中硬编码 API Key，始终通过环境变量管理

> 🚫 **请求频率**：请控制请求频率，避免触发频率限制

> 🌐 **数据来源**：所有新闻数据来自 [TianAPI](https://www.tianapi.com/)，版权归原作者所有

---

<div align="center">

### 🌟 如果这个项目对你有帮助，欢迎 Star！

Made with ❤️ for news readers

</div>
