# Interface Documentation

## Scope
IB Alpha Agent currently exposes a local Python / CLI research interface. It does **not** provide the HTTP user CRUD endpoints previously described in this file.

Repository behavior is governed by:
- `AGENTS.md` for autonomy, clarification, approval, and completion;
- `SKILL.md` for canonical equity-research methodology.

## CLI

### Research with autonomous read-only public research
```bash
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ"
```

### Research with optional manual inputs
```bash
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ" \
  --facts-file examples/facts_ruanze.json \
  --peers-file examples/peers_compute_power.json
```

### Disable public web research
```bash
python -m ib_alpha_agent.cli research \
  --company "润泽科技" \
  --ticker "300442.SZ" \
  --no-web-search
```

## Python entry points

### `ib_alpha_agent.models.FactsPack`
Represents the target company and optional manually supplied facts.

### `ib_alpha_agent.config.AgentConfig`
Controls model, output directory, reasoning effort, and whether read-only public web research is enabled.

### `ib_alpha_agent.orchestrator.run_research(facts, peers, cfg)`
Runs the canonical research flow and returns a `ResearchOutput`.

### `ib_alpha_agent.orchestrator.assess_completion(body, facts, web_research_enabled)`
Applies structural quality checks and returns:
- `COMPLETE`
- `COMPLETE_WITH_GAPS`
- `BLOCKED`

### `ib_alpha_agent.reporting.render_report(output, output_dir)`
Writes the local Markdown research report, including status, gaps, and quality checks.

## External-action boundary
The current research interface performs analysis and may use read-only public web research. It does not define or authorize endpoints for trading, payment, publication, user deletion, deployment, or other external consequential actions. Such actions remain separately approval-gated under `AGENTS.md` if they are ever added in the future.
