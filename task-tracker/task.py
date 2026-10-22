import json, os, sys
from datetime import datetime

FILE = "tasks.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def now():
    return datetime.now().isoformat(timespec="seconds")

def find(tasks, tid):
    for t in tasks:
        if t["id"] == tid:
            return t
    print("Task not found")
    sys.exit(1)

def main():
    a = sys.argv[1:]
    if not a:
        print("Usage: add | update | delete | mark-in-progress | mark-done | list")
        return
    cmd, tasks = a[0], load()
    try:
        if cmd == "add":
            tid = max([t["id"] for t in tasks], default=0) + 1
            tasks.append({"id": tid, "description": a[1], "status": "todo",
                          "createdAt": now(), "updatedAt": now()})
            print(f"Task added successfully (ID: {tid})")
        elif cmd == "update":
            t = find(tasks, int(a[1]))
            t["description"], t["updatedAt"] = a[2], now()
            print("Task updated")
        elif cmd == "delete":
            tasks.remove(find(tasks, int(a[1])))
            print("Task deleted")
        elif cmd in ("mark-in-progress", "mark-done"):
            t = find(tasks, int(a[1]))
            t["status"], t["updatedAt"] = cmd[5:], now()
            print("Task marked as " + t["status"])
        elif cmd == "list":
            for t in tasks:
                if len(a) == 1 or t["status"] == a[1]:
                    print(f"[{t['id']}] {t['description']} - {t['status']}")
        else:
            print("Unknown command")
            return
    except (IndexError, ValueError):
        print("Invalid arguments")
        return
    save(tasks)

main()