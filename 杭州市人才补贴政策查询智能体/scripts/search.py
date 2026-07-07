#!/usr/bin/env python3
"""在知识库 Markdown 中按关键词检索，辅助智能体或命令行问答。"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "知识库"

# 领域关键词（用于无空格中文问句）
DOMAIN_KEYWORDS = [
    "生活补贴", "租房补贴", "青荷礼包", "青荷驿站", "青荷码", "春雨计划",
    "西部区县", "高层次人才", "异议处理", "创业", "中小微企业",
    "本科", "硕士", "博士", "大专", "应届", "非全日制",
    "上城", "拱墅", "西湖", "滨江", "钱塘", "萧山", "余杭", "临平",
    "富阳", "临安", "桐庐", "淳安", "建德",
]


def parse_keywords(query: str) -> list[str]:
    parts = [w for w in re.split(r"[\s,，、？?！!。]+", query.strip()) if w]
    keywords: list[str] = list(dict.fromkeys(parts))
    for kw in DOMAIN_KEYWORDS:
        if kw in query and kw not in keywords:
            keywords.append(kw)
    if not keywords and query.strip():
        keywords = [query.strip()]
    return keywords


def load_files(district: str | None = None) -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for path in sorted(KB.rglob("*.md")):
        rel = path.relative_to(KB)
        if district and district not in str(rel):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        files.append((rel, text))
    return files


def score(text: str, keywords: list[str]) -> int:
    lower = text.lower()
    s = 0
    for kw in keywords:
        k = kw.lower()
        s += lower.count(k) * 2
        if k in lower:
            s += 5
    return s


def extract_snippet(text: str, keyword: str, context: int = 120) -> str:
    idx = text.lower().find(keyword.lower())
    if idx < 0:
        return text[:200].replace("\n", " ") + "..."
    start = max(0, idx - context)
    end = min(len(text), idx + len(keyword) + context)
    snippet = text[start:end].replace("\n", " ")
    return re.sub(r"\s+", " ", snippet).strip()


def search(query: str, district: str | None = None, top: int = 5) -> list[dict]:
    keywords = parse_keywords(query)
    if not keywords:
        return []

    results: list[dict] = []
    for rel, text in load_files(district):
        s = score(text, keywords)
        if s <= 0:
            continue
        best_kw = max(keywords, key=lambda k: text.lower().count(k.lower()))
        results.append(
            {
                "file": str(rel),
                "score": s,
                "snippet": extract_snippet(text, best_kw),
            }
        )
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top]


def main() -> None:
    parser = argparse.ArgumentParser(description="检索杭州人才补贴知识库")
    parser.add_argument("query", help="检索关键词，如：富阳 生活补贴")
    parser.add_argument("--district", "-d", help="限定区县，如：萧山区")
    parser.add_argument("--top", "-n", type=int, default=5, help="返回条数")
    args = parser.parse_args()

    hits = search(args.query, args.district, args.top)
    if not hits:
        print("未找到匹配内容，请换关键词或补充知识库。")
        sys.exit(1)

    for i, hit in enumerate(hits, 1):
        print(f"\n[{i}] {hit['file']} (相关度 {hit['score']})")
        print(f"    {hit['snippet']}")


if __name__ == "__main__":
    main()
