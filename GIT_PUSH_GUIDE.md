# 🚀 医药合规问答系统 - Git 推送指南

## 当前状态

✅ Git 仓库已初始化
✅ 所有代码已提交（3个提交）
✅ 远程仓库已配置：https://github.com/3495857712-lang/resume.git
❌ 缺少 GitHub 认证信息

## 快速推送方案

### 方案一：使用 Personal Access Token（推荐）

在您的本地终端执行：

```bash
# 1. 克隆当前项目或创建临时目录
git clone https://github.com/3495857712-lang/resume.git
cd resume

# 2. 配置 Git 用户信息
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 3. 拉取最新代码并创建文件
# 复制以下核心文件到项目目录：
# - config/agent_llm_config.json
# - src/agents/agent.py
# - src/tools/knowledge_retrieval_tool.py
# - src/tools/compliance_checker_tool.py
# - src/tools/audit_logger_tool.py
# - requirements.txt

# 4. 提交
git add .
git commit -m "feat: 实现医药合规问答系统

- 集成知识库检索（RAG）能力
- 实现合规规则检查（禁止诊断/开处方）
- 完善审计日志记录
- 配置短期记忆管理
- 使用豆包大模型"

# 5. 推送（使用 Personal Access Token）
# 格式: https://<token>@github.com/用户名/仓库名.git
git push https://<YOUR_TOKEN>@github.com/3495857712-lang/resume.git main
```

### 方案二：GitHub Web 界面上传

**步骤 1**: 访问目标仓库
```
https://github.com/3495857712-lang/resume
```

**步骤 2**: 创建目录结构
- 点击 "Create new file"
- 输入 `config/agent_llm_config.json`（会自动创建 config 目录）
- 粘贴文件内容
- 点击 "Commit new file"

**步骤 3**: 重复上传所有文件
```
需要上传的文件：
├── config/agent_llm_config.json
├── src/agents/agent.py
├── src/tools/knowledge_retrieval_tool.py
├── src/tools/compliance_checker_tool.py
├── src/tools/audit_logger_tool.py
└── requirements.txt
```

### 方案三：GitHub CLI（如果已安装）

```bash
# 安装 GitHub CLI
# macOS: brew install gh
# Ubuntu: sudo apt install gh

# 登录
gh auth login

# 创建仓库并推送
gh repo create resume --public --source=. --push
```

### 方案四：SSH 密钥方式

```bash
# 1. 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your.email@example.com"

# 2. 查看公钥
cat ~/.ssh/id_ed25519.pub

# 3. 添加到 GitHub
# 访问 https://github.com/settings/keys
# 点击 "New SSH key"，粘贴公钥内容

# 4. 测试连接
ssh -T git@github.com

# 5. 推送
git remote set-url origin git@github.com:3495857712-lang/resume.git
git push -u origin main
```

## 📦 获取项目文件

### 方法 1：下载打包文件
当前环境已创建打包文件：`medical_agent_package.tar.gz`

### 方法 2：直接复制文件内容
所有源代码文件的完整内容都在当前目录中，可以逐个复制。

## ⚙️ 推送后配置

推送成功后，在目标服务器上：

```bash
# 1. 克隆仓库
git clone https://github.com/3495857712-lang/resume.git
cd resume

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
export COZE_WORKSPACE_PATH=$(pwd)
export COZE_WORKLOAD_IDENTITY_API_KEY=your_key
export COZE_INTEGRATION_MODEL_BASE_URL=your_url

# 4. 运行服务
python src/main.py
```

## 🔑 如何获取 Personal Access Token

1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择权限：`repo`（完整仓库访问权限）
4. 点击 "Generate token"
5. **立即复制 Token**（只显示一次）

## ✅ 验证推送成功

推送后访问：
```
https://github.com/3495857712-lang/resume
```

应该能看到以下提交：
```
feat: 实现医药合规问答系统
chore: 添加GitHub推送指南和代码打包
```

## 📞 需要帮助？

如果遇到问题，请提供：
1. 错误信息截图
2. 您使用的推送方式
3. GitHub 仓库权限确认

---
最后更新：2026-03-30
