#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> 杭州市人才补贴政策查询智能体 · 本地部署"
echo "    项目目录: $(pwd)"
echo

chmod +x scripts/search.py scripts/ask.py 2>/dev/null || true

echo "==> 验证 Python 检索"
python3 scripts/search.py "生活补贴" -n 2 | head -20
echo

echo "==> 验证本地问答"
python3 scripts/ask.py "余杭区本科补贴"
echo

echo "==> 部署完成"
echo
echo "使用方式："
echo "  1. Cursor：打开本文件夹或 杭州市人才补贴政策查询智能体.code-workspace"
echo "  2. 命令行：python3 scripts/ask.py \"你的问题\""
echo "  3. 交互：  python3 scripts/ask.py -i"
echo "  4. 检索：  python3 scripts/search.py \"关键词\""
