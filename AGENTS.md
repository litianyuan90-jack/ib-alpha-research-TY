# AGENTS.md

## Scope
This file governs how an agent operates in this repository. Domain-specific equity-research methodology belongs in `SKILL.md`.

Within this repository:
- `AGENTS.md` governs autonomy, clarification, approval boundaries, and task completion.
- `SKILL.md` is the single canonical source for research methodology and quality standards.
- Templates define presentation structure only; they must not create competing behavioral rules.
- Code should load or reference the canonical rules rather than maintain hand-copied substitutes.

## Default autonomy
For ordinary, reversible, read-only work, proceed to completion without asking for confirmation.

This includes:
- reading repository files and available context;
- public-source research and browsing;
- analysis, calculations, comparisons, and diagnostics;
- running non-destructive tests and checks;
- drafting reports, patches, plans, and working artifacts;
- making reversible edits on a working tree or feature branch when the user has explicitly asked to implement, fix, update, refactor, or modify the repository.

Do not ask for confirmation merely because:
- the task has multiple steps;
- there are several reasonable implementation choices;
- additional read-only research is needed;
- some non-critical information is missing;
- the next step is an ordinary continuation of an already-authorized task.

## Clarification policy
Ask a clarifying question only when all three conditions are true:
1. a material ambiguity remains after using available context and retrieval;
2. different plausible interpretations would materially change the outcome; and
3. proceeding on a reasonable stated assumption could create meaningful downside.

Otherwise:
- make the most reasonable assumption;
- state the assumption when it materially affects the result;
- continue the work.

When information is missing but non-blocking:
- mark it as unknown or unverified;
- lower confidence where appropriate;
- complete all work that can still be completed.

Missing evidence should normally reduce confidence, not stop execution.

## Explicit approval gates
Existing explicit approval requirements remain in force.

Explicit user approval is required before actions that create material external or irreversible consequences, including:
- sending, publishing, or posting content externally;
- contacting third parties;
- executing trades, purchases, payments, or binding commitments;
- deploying to production or changing live infrastructure;
- merging into, force-updating, or directly rewriting a protected/default branch when a reviewable branch or PR is available;
- deleting user data or irreversibly overwriting important files;
- changing permissions, credentials, secrets, security settings, or access controls;
- expanding the agent's authority beyond the boundaries currently stated in this file;
- any action explicitly designated elsewhere as approval-required.

A request to **review, audit, inspect, propose, preview, or draft** is not approval to apply changes.

A request to **implement, fix, update, refactor, modify, or execute** authorizes ordinary reversible repository edits and tests within the stated scope, preferably on a feature branch when the change is material. It does not by itself authorize merge, deployment, publication, or other external consequences.

Do not add extra confirmation gates for routine reversible work that is already within an authorized scope.

## Task completion
Do not stop after producing only a plan, outline, partial implementation, or first draft unless:
- the user specifically requested only that stage; or
- an explicit approval gate applies.

When blocked on one part of a task:
- complete every unblocked part;
- identify the remaining blocker precisely;
- request only the minimum decision or information required.

Do not report a task as complete merely because execution returned without an exception. Completion requires the stated deliverables and applicable quality checks to be satisfied.

Use these completion states when useful:
- `COMPLETE`: requested deliverables and required checks are satisfied.
- `COMPLETE_WITH_GAPS`: useful work is finished, but identified non-blocking evidence or quality gaps remain.
- `BLOCKED`: a material blocker prevents the core deliverable from being completed.

## Change-control safeguard
If a proposed edit would broaden the agent's permissions or reduce an existing approval requirement, surface that effect explicitly and obtain user approval before applying it.

When the user has explicitly approved a previously disclosed authority expansion, implement only that disclosed expansion; do not infer broader permission.
