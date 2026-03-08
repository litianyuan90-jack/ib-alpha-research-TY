# IB Alpha Agent v3

面向股票深度研究的模块化 AI 投研代理。

## 核心升级
- 模块化 orchestration
- 可替换数据源适配器
- 估值与可比公司骨架
- Markdown 报告渲染
- CLI 命令行入口
- 手工 facts pack 输入机制

## 快速开始
```bash
pip install -r requirements.txt
cp .env.example .env
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ" \
  --facts-file examples/facts_ruanze.json \
  --peers-file examples/peers_compute_power.json
```
