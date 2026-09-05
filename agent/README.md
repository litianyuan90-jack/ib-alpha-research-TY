# Legacy Compatibility Entry Point

`agent/research_agent.py` 仅作为旧命令兼容入口保留；它不再维护独立 Skill 或 prompt，而是复用 `src/ib_alpha_agent/` 的 canonical v3 core。

## 推荐使用
```bash
pip install -e .
export OPENAI_API_KEY="your_key"

python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ"
```

## 旧命令仍可使用
```bash
python agent/research_agent.py \
  --company "润泽科技" \
  --ticker "300442.SZ"
```

默认启用只读公开 web research；可用 `--no-web-search` 关闭。

## Canonical rules
- `AGENTS.md`：自主性、澄清、批准、完成规则。
- `SKILL.md`：唯一投研方法论与质量标准。

不要在 `agent/` 目录重新创建独立 Skill、system prompt 或批准规则。
