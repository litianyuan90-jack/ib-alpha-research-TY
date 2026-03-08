# IB Alpha Research TY

投行级股票研究框架 + AI 投研代理（Research Agent）脚手架。

## 项目结构

```text
ib-alpha-research-pro/
├─ README.md
├─ LICENSE
├─ skill/
│  └─ IB_ALPHA_SKILL_V2.md
├─ industry-maps/
│  └─ china-computing-power-map-2026.md
├─ templates/
│  ├─ prompt-template.md
│  ├─ output-template.md
│  └─ diligence-checklist.md
├─ examples/
│  └─ ruanze-tech-example.md
└─ agent/
   ├─ README.md
   ├─ requirements.txt
   ├─ config.example.json
   └─ research_agent.py
```

## 这个仓库能做什么

### 1. 作为手动研究框架使用
把 `templates/prompt-template.md` 复制给 AI，并替换公司名与股票代码。

### 2. 作为 ChatGPT / Custom GPT 的系统提示词使用
把 `skill/IB_ALPHA_SKILL_V2.md` 作为核心指令，配合模板一起使用。

### 3. 作为 AI 投研代理的代码基础
`agent/research_agent.py` 提供一个最小可运行脚手架：
- 输入公司名称 / 股票代码
- 自动拼装研究提示词
- 调用 OpenAI Responses API
- 输出 Markdown 研究报告

## 快速开始

### 手动方式
1. 打开 `templates/prompt-template.md`
2. 替换目标公司
3. 发给 AI
4. 用 `templates/output-template.md` 检查输出质量

### 代码方式
1. 在 `agent/config.example.json` 基础上建立你自己的配置文件
2. 设置环境变量 `OPENAI_API_KEY`
3. 安装依赖：
   ```bash
   pip install -r agent/requirements.txt
   ```
4. 运行：
   ```bash
   python agent/research_agent.py --company "润泽科技" --ticker "300442.SZ"
   ```

## 发布到 GitHub 的建议步骤
1. 新建公开仓库
2. 上传整个目录
3. 提交信息：
   `feat: initialize IB Alpha Research TY`
4. 在仓库 About 里补充 topics：
   `equity-research`, `investment`, `ai-agent`, `a-shares`, `valuation`

## 注意
- 这个仓库是 GitHub-ready，但不会自动推送到你的 GitHub 账号
- `agent/` 是起步版脚手架，适合后续继续接入财报抓取、RAG、估值模型和行业数据库
