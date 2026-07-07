# 杭州市人才补贴政策查询智能体

专注回答**杭州市及各区**人才补贴、**青荷礼包**、**青荷驿站**、生活补贴、租房补贴等相关政策。

## 本地部署

### 一键安装验证

```bash
cd 杭州市人才补贴政策查询智能体   # 或克隆后的目录名
bash scripts/setup.sh
```

要求：**Python 3.9+**（仅用标准库，无需 pip 安装依赖）

### 命令行问答

```bash
# 单次提问
python3 scripts/ask.py "本科在余杭刚缴社保能领什么"

# 限定区县
python3 scripts/ask.py "租房补贴续领" --district 萧山区

# 交互模式
python3 scripts/ask.py -i
```

### 知识库检索

```bash
python3 scripts/search.py "青荷礼包"
python3 scripts/search.py "富阳 生活补贴" -n 5
```

### Cursor 智能体（推荐）

1. **File → Open Workspace from File** → 选择 `杭州市人才补贴政策查询智能体.code-workspace`
2. 新建 Agent 对话，直接提问

智能体自动读取 `.cursorrules` 与 `知识库/`。

## 目录结构

```
├── .cursorrules                 # 智能体系统提示词
├── .cursor/rules/               # Cursor 规则
├── 知识库/
│   ├── 00-索引.md
│   ├── 市级/                    # 生活补贴、租房补贴、青荷礼包、青荷驿站等
│   ├── 区级/                    # 余杭、萧山、富阳、滨江等
│   ├── FAQ.md
│   └── 来源与更新.md
└── scripts/
    ├── setup.sh                 # 本地部署脚本
    ├── ask.py                   # 本地问答
    └── search.py                # 知识库检索
```

## 准确性说明

- 回答优先引用 `知识库/` 结构化政策，并标注官方来源
- 政策可能调整，**以主管部门最新公告为准**
- 不确定处标注「建议核实」

## 官方咨询

- 杭州人社：**0571-96345**
- 青荷礼包：**0571-96225**
- 申报：[亲清在线](https://qinqing.hangzhou.gov.cn/) / 杭州市民卡 APP / 微信小程序「人才杭州」

## License

MIT

## 推送到 GitHub

仓库名称：**杭州市人才补贴政策查询智能体**

### 方式 1：GitHub 网页 + 命令行

1. 登录 [GitHub](https://github.com/new)，新建仓库  
   - 名称：`杭州市人才补贴政策查询智能体`  
   - 不要勾选「Initialize with README」（本地已有代码）

2. 在本项目目录执行：

```bash
export GITHUB_USER=你的GitHub用户名
bash scripts/push-github.sh
```

或手动：

```bash
git remote add origin https://github.com/你的用户名/杭州市人才补贴政策查询智能体.git
git push -u origin main
```

### 方式 2：GitHub CLI

```bash
gh auth login
gh repo create 杭州市人才补贴政策查询智能体 --public --source=. --remote=origin --push
```
