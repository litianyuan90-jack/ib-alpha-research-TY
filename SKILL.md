# IB-Alpha Research Skill v3.0

## Authority
This is the single canonical source for IB-Alpha equity-research methodology in this repository.

Execution behavior — autonomy, clarification, approval, and completion — is governed by `AGENTS.md`.
Templates may define output shape, but must not override or duplicate the methodology below.

## Purpose
Use this skill to produce institutional-grade equity research for listed companies, with a bias toward A-share technology, infrastructure, and manufacturing names.

The objective is not to accumulate information. It is to decide, with an explicit evidence chain:
1. Is this a structurally attractive industry?
2. Is this company a real winner within that industry?
3. Is the current valuation attractive?
4. Is the current timing favorable?
5. What would invalidate the thesis?

## Core analytical discipline
Keep these concepts separate:
- **good company**
- **good business**
- **good price**
- **good timing**

Do not confuse reported profit with recurring operating profit.
When material or applicable, distinguish:
- statutory earnings;
- adjusted earnings;
- cash earnings;
- asset-monetization gains;
- valuation-multiple expansion.

Never present inference as fact.
Never support a thesis with evidence that does not actually establish the claim.

## Evidence policy
Prefer primary sources whenever available and material:
- annual reports and interim / quarterly reports;
- exchange filings and company announcements;
- official investor presentations and transcripts;
- policy and regulatory documents;
- official competitor disclosures.

For every important conclusion:
- separate **Fact / Inference / Judgment**;
- identify material unknowns;
- indicate confidence when evidence is incomplete;
- use the latest relevant reporting period and make the research cutoff explicit.

If evidence is missing but the analysis can still proceed, mark the gap and reduce confidence rather than fabricating precision.

## Workflow

### Module 1: Industry structure
Assess:
- market size and growth;
- policy support and regulatory constraints;
- industry-chain position;
- barriers to entry;
- supplier and customer bargaining power;
- substitution risk;
- cycle stage.

Output:
- industry attractiveness score (1-5);
- industry phase: emerging / scaling / mature / declining;
- the two or three structural variables that matter most.

### Module 2: Business model
Map:
- revenue streams;
- pricing model;
- delivery model;
- customer profile and concentration;
- expansion engine;
- capex intensity;
- working-capital profile.

Output:
- business-model summary;
- key revenue-driver table;
- operating-leverage map.

### Module 3: Competitive moat
Assess moat through:
- resource access;
- technology;
- switching cost;
- ecosystem position;
- capital access;
- execution and delivery capability.

Output:
- moat matrix;
- moat durability rating;
- evidence that the moat is strengthening, stable, or eroding.

### Module 4: Financial quality
Analyze:
- revenue quality;
- gross margin / EBITDA / EBIT / net margin where relevant;
- recurring vs non-recurring profit;
- cash conversion;
- capex intensity;
- ROE / ROIC;
- leverage and liquidity;
- customer concentration;
- balance-sheet quality.

Output:
- normalized earnings bridge where material;
- financial red flags;
- operating-quality score.

### Module 5: Valuation
Use **at least two genuinely applicable valuation methods**. Use a third method when it adds decision value.

Possible methods:
- PE;
- EV/EBITDA;
- DCF;
- SOTP;
- PB / replacement cost / NAV;
- PEG;
- dividend yield / FFO / AFFO for appropriate asset-heavy models.

Rules:
- do not force an invalid method merely to meet a method count;
- use adjusted earnings when one-off gains are material;
- for capex-heavy businesses, do not rely only on PE;
- for platform-plus-asset models, consider SOTP when separable economics justify it;
- distinguish valuation upside caused by earnings growth from upside caused only by multiple expansion.

Output:
- bear / base / bull valuation range when inputs support it;
- key assumptions table;
- mispricing diagnosis;
- what the current price appears to imply.

### Module 6: Catalysts
Assess:
- earnings catalysts;
- asset monetization;
- policy catalysts;
- order / capacity / utilization inflection;
- margin improvement;
- financing or balance-sheet relief.

Output:
- 3-5 highest-probability catalysts;
- estimated timing window;
- observable evidence that would confirm each catalyst.

### Module 7: Risk map
Assess:
- macro risk;
- industry risk;
- technology substitution;
- execution risk;
- customer concentration;
- policy / compliance;
- financing / dilution;
- valuation de-rating.

Output:
- risk matrix with probability and impact;
- thesis-break conditions rather than generic disclaimers.

### Module 8: Capital-markets lens
Assess:
- current market narrative;
- what is already priced in;
- ownership structure where material;
- possible re-rating / de-rating drivers;
- sentiment sensitivity.

Output:
- consensus vs variant-view section;
- identify whether the variant view is evidence-backed or merely contrarian.

### Module 9: Management & governance
Assess:
- controller / promoter quality where relevant;
- capital-allocation record;
- incentives;
- related-party transactions;
- strategic consistency;
- credibility of disclosures.

Output:
- governance-quality note;
- major governance red flags if any.

### Module 10: Investment conclusion
Answer explicitly:
1. Is this a structurally good industry?
2. Is this company a real winner?
3. Is the current price attractive?
4. Is the current timing favorable?
5. What breaks the thesis?
6. What must be monitored quarterly?

Output:
- investment thesis in one paragraph;
- rating: Avoid / Watch / Accumulate on weakness / Core holding candidate;
- monitoring dashboard;
- what would change the conclusion.

## Required output structure
1. Executive Summary
2. Research Cutoff & Evidence Quality
3. Industry & Policy Backdrop
4. Business Model
5. Competitive Position
6. Financial Quality
7. Valuation
8. Catalysts
9. Risks
10. Management & Governance
11. Consensus vs Variant View
12. Final View
13. What Would Change My Mind
14. Five Metrics to Monitor
15. Unknowns / Follow-up Diligence

## Quality gate
Before calling a report complete, verify that:
- the target company and research cutoff are clear;
- major claims have an evidence basis;
- fact, inference, and judgment are distinguishable;
- recurring and non-recurring earnings are separated when material;
- valuation uses at least two applicable methods, or explains why fewer are genuinely usable;
- catalysts include timing and observable confirmation signals;
- risks include thesis-break conditions;
- unknowns are surfaced instead of silently guessed;
- the final conclusion answers company, price, timing, and thesis-break questions;
- five monitoring metrics are provided.

If one or more non-critical checks remain unresolved, label the result `COMPLETE_WITH_GAPS` rather than claiming full completion.

## Special add-on for computing power / AI infrastructure
When analyzing computing-power names, split the chain where relevant into:
- chips;
- servers;
- data center / IDC / AIDC;
- optical modules;
- network interconnect;
- liquid cooling / thermal management;
- power / UPS;
- cloud / scheduling platform;
- REIT / asset-monetization angle.

Then identify:
- which layer captures scarcity;
- which layer has the strongest margin structure;
- which layer has the best capital efficiency;
- which layer is currently most crowded in valuation;
- where narrative may be running ahead of monetization.
