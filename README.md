# IB Alpha Agent v3.1

面向股票深度研究的模块化 AI 投研代理。

## Governance
- `AGENTS.md`：自主性、澄清、批准边界、任务完成规则。
- `SKILL.md`：唯一 canonical 投研方法论与质量标准。
- `templates/`：只定义展示与任务入口，不维护独立行为规则。
- `src/ib_alpha_agent/`：执行 canonical 规则，不复制另一套 system prompt。

默认允许只读公开资料检索，以减少“先人工准备 facts pack 才能开始”的不必要阻断。外部发布、交易、部署、默认分支合并等后果性动作仍保留明确批准要求。

## 核心能力
- 模块化 orchestration
- 可选人工 facts pack / peers pack
- 缺少人工 facts pack 时可自主进行只读公开资料研究
- 估值与可比公司骨架
- `COMPLETE / COMPLETE_WITH_GAPS / BLOCKED` 完成状态
- Markdown 报告渲染
- CLI 命令行入口

## 快速开始
```bash
pip install -e .
export OPENAI_API_KEY="your_key"

python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ"
```

默认启用公开 web research。若已有人工事实包：
```bash
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ" \
  --facts-file examples/facts_ruanze.json \
  --peers-file examples/peers_compute_power.json
```

如需完全关闭公开 web research：
```bash
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ" \
  --no-web-search
```

## 行为原则
普通、可逆、只读工作默认继续执行，不因多步骤、合理实现选择或非关键资料缺口反复要求确认。资料不足通常应降低置信度并列入 Unknowns，而不是停止整个任务。

明确批准仍用于具有外部或不可逆后果的动作。详见 `AGENTS.md`。
