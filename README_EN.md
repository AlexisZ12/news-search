<div align="center">

# News Search

A clean and efficient CLI tool for searching news articles via TianAPI by category and keyword 📰

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-brightgreen?logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.x-green)](https://docs.python-requests.org/)
[![TianAPI](https://img.shields.io/badge/TianAPI-AllNews-orange)](https://www.tianapi.com/)

[**简体中文**](README.md) | English

</div>

---

## ✨ Features

- 🔍 **Category Search** - 26 news categories covering tech, finance, sports, military, and more
- 🎯 **Keyword Filtering** - Precise matching of articles containing specified keywords
- 📊 **Adjustable Results** - Flexible result count, up to 50 items
- 🖥️ **CLI Friendly** - Clean argument design, easy to integrate and automate
- 🌐 **Rich Data** - Returns title, description, publish time, source, cover image, and more

---

## 🚀 Quick Start

### 📦 Install Dependencies

```bash
pip install requests
```

### 🔑 Get API Key

1. Sign up at [TianAPI](https://www.tianapi.com/) (free registration)
2. Get your API Key from the dashboard
3. Set the environment variable:

```bash
export TIAN_API_KEY="your_api_key"
```

> 💡 Add the above to `~/.zshrc` or `~/.bashrc` for persistence

### 🎮 Basic Usage

```bash
# View help 👀
python scripts/news_search.py --help

# Search AI-related news 🔍
python scripts/news_search.py -c ai -k "deep learning"

# Search domestic news, return 20 results 📈
python scripts/news_search.py -c guonei -k "economy" -n 20
```

---

## 📖 Usage Guide

### 🔧 Arguments

| Argument | Shorthand | Required | Default | Description |
|:--------:|:---------:|:--------:|:-------:|-------------|
| `--col` | `-c` | Yes | — | News category (nameid or numeric colid) |
| `--keyword` | `-k` | Yes | — | Search keyword(s) |
| `--num` | `-n` | No | 10 | Number of results, range 1–50 |

### 💡 Examples

```bash
# 🤖 AI domain search
python scripts/news_search.py -c ai -k "LLM"

# 📱 Tech news search
python scripts/news_search.py -c keji -k "chip" -n 20

# 🏀 Sports news search
python scripts/news_search.py -c nba -k "playoffs"

# 💰 Finance news search
python scripts/news_search.py -c caijing -k "green energy"

# 🔢 By numeric colid (tech = 13)
python scripts/news_search.py -c 13 -k "AI"
```

---

## 📂 Supported Categories

| nameid | Category | colid |
|:------:|:--------:|:-----:|
| `social` | Social News | 5 |
| `guonei` | Domestic News | 7 |
| `world` | World News | 8 |
| `huabian` | Entertainment | 10 |
| `tiyu` | Sports | 12 |
| `keji` | Tech News | 13 |
| `health` | Health | 17 |
| `travel` | Travel | 18 |
| `apple` | Apple News | 19 |
| `nba` | NBA News | 20 |
| `vr` | VR Tech | 21 |
| `it` | IT News | 22 |
| `football` | Football News | 26 |
| `military` | Military News | 27 |
| `ai` | AI News | 29 |
| `cba` | CBA News | 30 |
| `game` | Gaming | 31 |
| `caijing` | Finance | 32 |
| `dongman` | Anime | 33 |
| `internet` | Internet | 34 |
| `auto` | Auto News | 35 |
| `sicprobe` | Science | 36 |
| `film` | Film & TV | 40 |
| `huanbao` | Environment | 41 |
| `lajifenleinews` | Waste Sorting | 42 |
| `woman` | Women | 43 |
| `nongye` | Agriculture | 44 |
| `esports` | Esports | 45 |
| `petnews` | Pets | 46 |

---

## 📊 Output Example

```
Domestic LLM releases surge as AI applications accelerate
Recently, multiple tech companies have launched self-developed large language
models covering chat, coding, text-to-image, and more, marking China's AI
industry entering an accelerated application phase.
2026-05-04 09:30:00
Source: Science Daily
https://example.com/news/12345
```

Each article returns the following fields:

| Field | Description |
|:-----:|-------------|
| `title` | Article title |
| `description` | Article summary |
| `ctime` | Publish time |
| `url` | Article URL |
| `picUrl` | Cover image URL |
| `source` | News source |

---

## 🛠️ API Reference

This tool calls the TianAPI AllNews endpoint:

```
POST https://apis.tianapi.com/allnews/index
Content-Type: application/x-www-form-urlencoded

key=<API_KEY>&col=<colid>&word=<keyword>&num=<1-50>
```

### Error Codes

| Code | Meaning |
|:----:|---------|
| 200 | Success |
| 10001 | Invalid API Key |
| 10002 | Insufficient credits |
| 10003 | API expired or disabled |
| 10004 | Rate limit exceeded |

---

## 📁 Project Structure

```
news-search/
├── README.md
├── README_EN.md
├── SKILL.md
└── scripts/
    └── news_search.py
```

---

## ⚠️ Notes

> 📌 **API Limits**: Free accounts have daily request quotas — use responsibly

> 🔑 **Key Security**: Never hardcode your API Key; always use environment variables

> 🚫 **Rate Limits**: Control request frequency to avoid triggering rate limits

> 🌐 **Data Source**: All news data comes from [TianAPI](https://www.tianapi.com/); copyright belongs to original authors

---

<div align="center">

### 🌟 If this project helps you, give it a Star!

Made with ❤️ for news readers

</div>
