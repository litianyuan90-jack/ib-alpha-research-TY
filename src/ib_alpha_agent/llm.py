from __future__ import annotations
import os
from openai import OpenAI


def run_llm(
    instructions: str,
    prompt: str,
    model: str = "gpt-5",
    reasoning_effort: str = "medium",
    enable_web_search: bool = False,
) -> str:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    kwargs = {
        "model": model,
        "instructions": instructions,
        "input": prompt,
        "reasoning": {"effort": reasoning_effort},
    }
    if enable_web_search:
        kwargs["tools"] = [{"type": "web_search"}]

    response = client.responses.create(**kwargs)
    return getattr(response, "output_text", None) or str(response)
