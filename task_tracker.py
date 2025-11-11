# task_tracker.py
# Simple in-memory Task Tracker with optional JSON persistence.

import json, os
DB = "tasks.json"
tasks = []  # list of {"task": str, "done": bool}

def load():
    global tasks
    if os.path.exists(DB):
        with open(DB, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save():
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(text: str):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Task text must be a non-empty string.")
    tasks.append({"task": text.strip(), "done": False})

def list_tasks() -> list:
    # return a copy (don’t leak internal list)
    return [{"task": t["task"], "done": t["done"]} for t in tasks]

def complete_task(index: int):
    if not (1 <= index <= len(tasks)):
        raise IndexError("Task index out of range.")
    tasks[index - 1]["done"] = True
