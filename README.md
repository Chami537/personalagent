# Personal Knowledge Agent

一个基于 Obsidian Markdown 笔记的个人知识问答助手。项目按阶段实现，从本地命令行 RAG 开始，再逐步加入 API、Agent、Docker、云端部署和 QQ Bot。

## 当前进度

- [x] 创建 Python 虚拟环境（Python 3.12.3）
- [x] 创建 `requirements.txt` 并安装依赖
- [x] 配置 `.gitignore`
- [ ] 选取 3～5 篇 Obsidian Markdown 测试笔记
- [ ] 完成本地命令行 RAG

目前还没有实现 `main.py`、RAG 流程或 API 服务。

## 第一版技术栈

- Python 3.12
- LangChain：组织文档加载、切分、检索和模型调用
- `BAAI/bge-small-zh-v1.5`：计划使用的本地中文 embedding 模型
- Chroma：计划用于本地保存向量、文本片段和来源信息
- OpenAI-compatible LLM API：生成基于检索内容的回答
- 命令行：第一版通过 `python main.py` 运行

## 第一版 RAG 流程

```text
Obsidian Markdown
    → 文档加载与切分
    → 本地 embedding
    → Chroma 向量库
    → Retriever 检索相关片段
    → LLM 生成回答
    → 返回答案、来源文件和检索片段
```

本地 embedding 不需要把整批笔记发送给 embedding API。向 LLM 提问时，检索到的片段会发送给配置的 LLM 服务。

## 开发环境

在 Ubuntu 终端进入项目目录，并激活虚拟环境：

```bash
cd ~/projects/personal_agent
source .venv/bin/activate
```

创建新环境时运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

本地 embedding 模型将在 RAG 首次加载模型时下载。LLM 的 API 配置将在后续步骤加入本地 `.env` 文件；不要把密钥提交到 Git。

## 测试笔记

第一版只使用 3～5 篇经过挑选的 Markdown 笔记，放在 `data/sample_notes/`。该目录和生成的 `chroma_db/` 已加入 `.gitignore`，不会随项目提交。

## 开发路线

1. 本地 Markdown RAG 命令行问答
2. 使用 FastAPI 提供 `POST /chat`
3. 加入包含少量工具的 Agent
4. 使用 Docker Compose 运行服务
5. 部署到 Ubuntu 云服务器
6. 通过 OneBot 或 QQ Bot 框架接入 QQ
