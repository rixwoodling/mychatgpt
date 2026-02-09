#!/usr/bin/env python3
import openai
import sys
from pathlib import Path

# Read the key
key_path = Path("openai.key")
openai.api_key = key_path.read_text().strip()

def ask(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = sys.stdin.read()

    print(ask(prompt))

