from __future__ import annotations
import os
from openai import OpenAI

def run_llm(instructions: str, prompt: str, model: str = "gpt-5", reasoning_effort: str = "medium") -> str:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
        reasoning={"effort": reasoning_effort},
    )
    return getattr(response, "output_text", None) or str(response)
