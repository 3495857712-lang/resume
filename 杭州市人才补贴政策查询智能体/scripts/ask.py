#!/usr/bin/env python3
"""本地问答：基于知识库关键词检索，输出相关政策摘要。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from search import search  # noqa: E402


def answer(query: str, district: str | None = None, top: int = 3) -> str:
    hits = search(query, district, top)

    if not hits:
        return (
            "知识库中未找到直接匹配内容。\n"
            "建议：换关键词（如「生活补贴」「青荷礼包」「余杭」），或在 Cursor 中打开本项目使用完整智能体。"
        )

    lines = [f"## 查询：{query}\n"]
    for i, hit in enumerate(hits, 1):
        lines.append(f"### [{i}] 知识库/{hit['file']}（相关度 {hit['score']}）\n")
        lines.append(f"{hit['snippet']}\n")
        lines.append(f"> 完整内容请阅读：`知识库/{hit['file']}`\n")

    lines.append("---")
    lines.append("政策以官方最新公告为准。咨询：0571-96345 | 亲清在线")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="杭州人才补贴政策本地问答")
    parser.add_argument("query", nargs="?", help="问题，如：本科余杭刚缴社保能领什么")
    parser.add_argument("--district", "-d", help="限定区县，如：余杭区")
    parser.add_argument("--top", "-n", type=int, default=3)
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")
    args = parser.parse_args()

    if args.interactive or not args.query:
        print("杭州人才补贴政策查询（本地知识库）")
        print("输入问题，空行退出。示例：青荷礼包怎么领\n")
        while True:
            try:
                q = input("你> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n再见。")
                break
            if not q:
                break
            print(answer(q, args.district, args.top))
            print()
        return

    print(answer(args.query, args.district, args.top))


if __name__ == "__main__":
    main()
