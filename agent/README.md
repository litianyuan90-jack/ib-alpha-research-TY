# AI Research Agent

这是一个最小可运行的 AI 投研代理脚手架。

## 功能
- 读取 skill 和模板
- 根据公司名称 / 股票代码自动拼装研究提示
- 调用 OpenAI Responses API
- 输出 Markdown 报告到本地

## 使用
```bash
export OPENAI_API_KEY=your_key
pip install -r requirements.txt
python research_agent.py --company "润泽科技" --ticker "300442.SZ"
```

## 后续建议升级
- 接入财报下载
- 接入公告解析
- 接入行业数据库
- 加入估值表自动计算
- 加入多公司横向对比
