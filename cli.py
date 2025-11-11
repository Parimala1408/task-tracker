# cli.py
# Very simple CLI wrapper so we can call functions via GitHub Codespaces or runner.

import sys
from task_tracker import add_task, list_tasks, complete_task

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python cli.py add \"Task text\"")
        print("  python cli.py list")
        print("  python cli.py done <index>")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "add":
        text = " ".join(sys.argv[2:]).strip()
        if not text:
            print("Please provide a task description.")
            sys.exit(1)
        add_task(text)
        print("Added:", text)
    elif cmd == "list":
        for i, t in enumerate(list_tasks(), 1):
            mark = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} {mark}")
    elif cmd == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Please provide a numeric task index.")
            sys.exit(1)
        complete_task(int(sys.argv[2]))
        print("Marked done:", sys.argv[2])
    else:
        print("Unknown command:", cmd)
        sys.exit(1)

if __name__ == "__main__":
    main()
