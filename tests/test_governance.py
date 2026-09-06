from __future__ import annotations
import unittest

from ib_alpha_agent.models import FactsPack
from ib_alpha_agent.orchestrator import assess_completion
from ib_alpha_agent.prompts import SKILL_PATH, SYSTEM_PROMPT


COMPLETE_BODY = """
# Executive Summary
# Research Cutoff & Evidence Quality
# Industry & Policy Backdrop
# Business Model
# Competitive Position
# Financial Quality
# Valuation
# Catalysts
# Risks
# Management & Governance
# Consensus vs Variant View
# Final View
# What Would Change My Mind
# Five Metrics to Monitor
# Unknowns / Follow-up Diligence
Fact / Inference / Judgment
""" + ("evidence " * 150)


class GovernanceTests(unittest.TestCase):
    def test_runtime_prompt_is_canonical_skill(self):
        self.assertEqual(SYSTEM_PROMPT, SKILL_PATH.read_text(encoding="utf-8").strip())

    def test_complete_when_structure_and_evidence_channel_pass(self):
        status, gaps, checks = assess_completion(
            COMPLETE_BODY,
            FactsPack(company="Example Co"),
            web_research_enabled=True,
        )
        self.assertEqual(status, "COMPLETE")
        self.assertEqual(gaps, [])
        self.assertTrue(all(checks.values()))

    def test_missing_facts_does_not_block_when_web_search_is_disabled(self):
        status, gaps, checks = assess_completion(
            COMPLETE_BODY,
            FactsPack(company="Example Co"),
            web_research_enabled=False,
        )
        self.assertEqual(status, "COMPLETE_WITH_GAPS")
        self.assertFalse(checks["evidence_channel"])
        self.assertTrue(any("facts pack" in gap for gap in gaps))

    def test_short_output_is_blocked(self):
        status, gaps, checks = assess_completion(
            "Valuation Risks",
            FactsPack(company="Example Co", facts={"source": "manual"}),
            web_research_enabled=False,
        )
        self.assertEqual(status, "BLOCKED")
        self.assertFalse(checks["substantive_output"])
        self.assertTrue(gaps)


if __name__ == "__main__":
    unittest.main()
