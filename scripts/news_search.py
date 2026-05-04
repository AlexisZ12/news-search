import requests
import argparse
import os
import sys

COL_MAP = {
    "social": 5,
    "guonei": 7,
    "world": 8,
    "huabian": 10,
    "tiyu": 12,
    "keji": 13,
    "health": 17,
    "travel": 18,
    "apple": 19,
    "nba": 20,
    "vr": 21,
    "it": 22,
    "football": 26,
    "military": 27,
    "ai": 29,
    "cba": 30,
    "game": 31,
    "caijing": 32,
    "dongman": 33,
    "internet": 34,
    "auto": 35,
    "sicprobe": 36,
    "film": 40,
    "huanbao": 41,
    "lajifenleinews": 42,
    "woman": 43,
    "nongye": 44,
    "esports": 45,
    "petnews": 46,
}

def main():
    parser = argparse.ArgumentParser(description="Search news via TianAPI")
    parser.add_argument("-c", "--col", required=True, help="News category (name or colid)")
    parser.add_argument("-k", "--keyword", required=True, help="Search keyword")
    parser.add_argument(
        "-n", "--num", type=int, default=10, choices=range(1, 51),
        help="Number of results, 1-50 (default: 10)",
    )
    args = parser.parse_args()

    tian_api_key = os.environ.get("TIAN_API_KEY")
    if not tian_api_key:
        print("Error: TIAN_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    col = args.col
    if col in COL_MAP:
        col = COL_MAP[col]
    else:
        try:
            col = int(col)
        except ValueError:
            print(
                f"Error: unknown category '{args.col}'. "
                f"Available names: {', '.join(COL_MAP)}",
                file=sys.stderr,
            )
            sys.exit(1)

    response = requests.post(
        "https://apis.tianapi.com/allnews/index",
        data={"key": tian_api_key, "col": col, "word": args.keyword, "num": args.num},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    data = response.json()

    if data.get("code") != 200:
        print(f"API error: {data.get('msg', 'unknown error')}", file=sys.stderr)
        sys.exit(1)

    result = data.get("result", {})
    newslist = result.get("newslist") or result.get("list") or []
    for item in newslist:
        print(item.get("title", ""))
        print(item.get("description", ""))
        print()

if __name__ == "__main__":
    main()
