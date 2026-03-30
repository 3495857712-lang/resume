# 医药合规问答系统 - GitHub 推送指南

## 项目信息
- 目标仓库: https://github.com/3495857712-lang/resume.git
- Agent名称: Medical Compliance QA Agent
- 创建时间: 2026-03-30

## 手动推送步骤

### 方式一：使用 Git 命令行

1. **在本地克隆目标仓库**
```bash
git clone https://github.com/3495857712-lang/resume.git
cd resume
```

2. **复制项目文件**
将以下文件和目录复制到仓库中：

```
resume/
├── config/
│   └── agent_llm_config.json
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── audit_logger_tool.py
│   │   ├── compliance_checker_tool.py
│   │   └── knowledge_retrieval_tool.py
│   └── storage/
│       └── memory/
│           └── memory_saver.py
├── requirements.txt
└── README.md
```

3. **提交并推送**
```bash
git add .
git commit -m "feat: 实现医药合规问答系统

功能特性：
- 集成知识库检索（RAG）能力
- 实现合规规则检查（禁止诊断/开处方）
- 完善审计日志记录
- 配置短期记忆管理
- 使用豆包大模型

新增文件：
- src/tools/knowledge_retrieval_tool.py
- src/tools/compliance_checker_tool.py
- src/tools/audit_logger_tool.py
- src/agents/agent.py
- config/agent_llm_config.json"

git push origin main
```

### 方式二：使用 GitHub Desktop

1. 打开 GitHub Desktop
2. Clone 仓库: https://github.com/3495857712-lang/resume.git
3. 将项目文件复制到仓库目录
4. 在左侧 Changes 面板填写提交信息
5. 点击 "Push origin" 按钮

### 方式三：使用 GitHub Web 界面

1. 访问 https://github.com/3495857712-lang/resume
2. 点击 "Add file" → "Upload files"
3. 拖拽文件或文件夹上传
4. 填写提交信息并点击 "Commit changes"

## 环境配置说明

推送后，在目标服务器上需要配置：

### 必需的环境变量
```bash
export COZE_WORKSPACE_PATH=/path/to/project
export COZE_WORKLOAD_IDENTITY_API_KEY=your_api_key
export COZE_INTEGRATION_MODEL_BASE_URL=your_base_url
```

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行服务
```bash
python src/main.py
# 或
bash scripts/http_run.sh
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `src/agents/agent.py` | Agent主逻辑，包含build_agent方法 |
| `src/tools/knowledge_retrieval_tool.py` | 知识库检索工具 |
| `src/tools/compliance_checker_tool.py` | 合规规则检查工具 |
| `src/tools/audit_logger_tool.py` | 审计日志记录工具 |
| `config/agent_llm_config.json` | LLM配置和System Prompt |
| `requirements.txt` | Python依赖包 |

## 注意事项

1. **敏感信息**: 请勿将API Key等敏感信息推送到GitHub
2. **日志目录**: 确保 `/app/work/logs/bypass/` 目录存在且可写
3. **知识库**: 首次运行需要导入医药知识库文档
4. **权限**: 确保对目标仓库有推送权限

## 验证推送成功

推送后可通过以下方式验证：

```bash
# 克隆到临时目录测试
git clone https://github.com/3495857712-lang/resume.git /tmp/test-clone
cd /tmp/test-clone

# 检查文件完整性
ls -R src/ config/

# 检查最新提交
git log -1 --stat
```

## 联系支持

如遇到问题，请检查：
1. GitHub仓库权限
2. 网络连接
3. Git配置（用户名、邮箱）
