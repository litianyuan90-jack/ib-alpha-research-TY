# Architecture

1. Load repository governance from `AGENTS.md`.
2. Load the single canonical research methodology from `SKILL.md`.
3. Load config.
4. Build the target company context:
   - load an optional manual facts pack; or
   - construct a minimal target context from company / ticker.
5. Load an optional peers pack.
6. Build the research brief.
7. Run LLM synthesis, with read-only public web research enabled by default unless explicitly disabled.
8. Run valuation and comparable helpers.
9. Evaluate structural quality and assign `COMPLETE`, `COMPLETE_WITH_GAPS`, or `BLOCKED`.
10. Render the final Markdown report with gaps and quality checks surfaced.

Templates are presentation aids only. They do not define independent research or approval rules.
