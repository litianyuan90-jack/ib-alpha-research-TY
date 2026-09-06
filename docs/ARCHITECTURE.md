# IB Alpha Agent Architecture

## Purpose
This repository is a modular equity-research agent, not a frontend/backend/database microservice application.

## Instruction hierarchy
- `AGENTS.md` governs autonomy, clarification, approval boundaries, and task completion.
- `SKILL.md` is the single canonical equity-research methodology and quality standard.
- `templates/` defines presentation structure only.
- Runtime code loads or references canonical rules instead of maintaining separate copies.

## Runtime flow
1. Parse target company / ticker and optional input files.
2. Load optional manual facts pack and peers pack.
3. If no manual facts pack is supplied, continue with target context rather than stopping.
4. Build the research prompt from the canonical `SKILL.md`.
5. Use read-only public web research by default unless `--no-web-search` is set.
6. Generate the research body.
7. Run valuation / comparable helper logic.
8. Run structural completion checks.
9. Assign one of:
   - `COMPLETE`
   - `COMPLETE_WITH_GAPS`
   - `BLOCKED`
10. Render Markdown with status, remaining gaps, and quality checks visible.

## Approval boundary
Research, reading, analysis, and other reversible work may proceed autonomously within an authorized task. External publication, trades, payments, deployment, default-branch merge, destructive data changes, security changes, or any newly expanded authority remain approval-gated under `AGENTS.md`.

## Design principle
Missing non-critical evidence should reduce confidence and appear as an explicit gap; it should not automatically stop the entire research task.
