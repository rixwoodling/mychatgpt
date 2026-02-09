#!/usr/bin/env python3
import openai
import datetime
import json
from pathlib import Path

# Load key
openai.api_key = Path("openai.key").read_text().strip()

HIST_FILE = Path("chat_history.json")

def load_history():
    if HIST_FILE.exists():
        try:
            return json.loads(HIST_FILE.read_text())
        except:
            return []
    return []

def save_history(history):
    HIST_FILE.write_text(json.dumps(history, indent=2))

history = load_history()

def timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def ask(prompt):
    history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )

    msg = response.choices[0].message.content
    history.append({"role": "assistant", "content": msg})

    save_history(history)
    return msg

print("Type 'exit' to leave the digital campfire.\n")

while True:
    try:
        prompt = input(f"(chatgpt) [{timestamp()}] > ")
    except KeyboardInterrupt:
        print()
        continue

    if prompt.strip().lower() in ["exit", "quit"]:
        break

    if not prompt.strip():
        continue

    answer = ask(prompt)
    print("\n" + answer + "\n")
