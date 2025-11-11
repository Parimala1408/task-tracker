# task_tracker.py
# Task Tracker with JSON persistence.

import json, os
DB = "tasks.json"
tasks = []

def load():
    """Load tasks from JSON file into memory."""
    global tasks
    if os.path.exists(DB):
        with open(DB, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    tasks = [
                        {"task": str(item.get("task", "")).strip(), "done": bool(item.get("done", False))}
                        for item in data
                    ]
                else:
                    tasks = []
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save():
    """Persist in-memory tasks to JSON file."""
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(text: str):
    load()
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Task text must be a non-empty string.")
    tasks.append({"task": text.strip(), "done": False})
    save()

def list_tasks() -> list:
    load()
    return [{"task": t["task"], "done": t["done"]} for t in tasks]

def complete_task(index: int):
    load()
    if not (1 <= index <= len(tasks)):
        raise IndexError("Task index out of range.")
    tasks[index - 1]["done"] = True
    save()
