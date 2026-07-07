#!/usr/bin/env bash
# 将本项目推送到 GitHub 仓库：杭州市人才补贴政策查询智能体
set -euo pipefail
cd "$(dirname "$0")/.."

REPO_NAME="杭州市人才补贴政策查询智能体"
GITHUB_USER="${GITHUB_USER:-}"

if [[ -z "${GITHUB_USER}" ]]; then
  echo "请设置 GitHub 用户名，例如："
  echo "  export GITHUB_USER=你的用户名"
  exit 1
fi

REMOTE="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

if git remote get-url origin &>/dev/null; then
  echo "已存在 origin: $(git remote get-url origin)"
else
  git remote add origin "${REMOTE}"
  echo "已添加 remote: ${REMOTE}"
fi

echo "==> 推送到 GitHub..."
git push -u origin main

echo
echo "完成！仓库地址："
echo "  https://github.com/${GITHUB_USER}/${REPO_NAME}"
