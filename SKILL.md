---
name: news-search
description: Search news articles from TianAPI by category and keyword. Outputs results to stdout.
---

# News Search Skill

A command-line tool for searching news articles via TianAPI by news category and search keyword.

## Purpose

Retrieve news articles from 29 Chinese news categories including tech, sports, finance, entertainment, and more. Useful for news monitoring, topic tracking, and content aggregation.

## Dependencies

```bash
pip install requests
```

## Command Reference

### Basic Syntax

```bash
python scripts/news_search.py --col <category> --keyword <keywords>
```

### Arguments

| Argument | Shorthand | Required | Default | Description |
|----------|-----------|----------|---------|-------------|
| `--col` | `-c` | Yes | — | News category name (nameid) or numeric colid |
| `--keyword` | `-k` | Yes | — | Search keyword(s) for filtering news articles |
| `--num` | `-n` | No | 10 | Number of results to return, range 1–50 |

## Available Categories

| nameid | 中文名 | colid |
|--------|--------|-------|
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

## Usage Examples

### Search by category name

```bash
# AI news containing "深度学习"
python scripts/news_search.py --col ai --keyword "深度学习"

# Domestic news containing "经济"
python scripts/news_search.py -c guonei -k "经济"
```

### Search by numeric colid

```bash
# Tech news (colid=13) containing "芯片"
python scripts/news_search.py --col 13 --keyword "芯片"
```