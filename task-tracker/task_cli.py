import json
import os
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Read tasks from the JSON file. Create the file if it doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {TASKS_FILE} is not valid JSON. Fix or delete it.")
        sys.exit(1)


def save_tasks(tasks):
    """Write the full task list to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def now():
    return datetime.now().isoformat(timespec="seconds")


def next_id(tasks):
    """Use max ID + 1 so IDs are never reused after a delete."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def parse_id(value):
    """Convert the ID argument to an int, or exit with a clear message."""
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid task ID (must be a number).")
        sys.exit(1)


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    print(f"Error: Task with ID {task_id} not found.")
    sys.exit(1)

def add_task(description):
    if not description.strip():
        print("Error: Description cannot be empty.")
        sys.exit(1)
    tasks = load_tasks()
    task = {
        "id": next_id(tasks),
        "description": description.strip(),
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    if not description.strip():
        print("Error: Description cannot be empty.")
        sys.exit(1)
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    task["description"] = description.strip()
    task["updatedAt"] = now()
    save_tasks(tasks)
    print(f"Task {task_id} updated successfully")

def delete_task(task_id):
    tasks = load_tasks()
    task = find_task(tasks, task_id)   # errors out if not found
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")                

def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    task["status"] = status
    task["updatedAt"] = now()
    save_tasks(tasks)
    print(f"Task {task_id} marked as {status}")


VALID_STATUSES = ("todo", "in-progress", "done")


def list_tasks(status=None):
    if status is not None and status not in VALID_STATUSES:
        print(f"Error: Unknown status '{status}'. Use: {', '.join(VALID_STATUSES)}")
        sys.exit(1)

    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['description']}")
        print(f"     Status: {t['status']} | Created: {t['createdAt']} | Updated: {t['updatedAt']}")


USAGE = """Usage:
  python task_cli.py add "description"
  python task_cli.py update <id> "new description"
  python task_cli.py delete <id>
  python task_cli.py mark-in-progress <id>
  python task_cli.py mark-done <id>
  python task_cli.py list [todo|in-progress|done]"""


def main():
    args = sys.argv[1:]          # skip the script name
    if not args:
        print(USAGE)
        sys.exit(1)

    command = args[0]

    if command == "add" and len(args) == 2:
        add_task(args[1])
    elif command == "update" and len(args) == 3:
        update_task(parse_id(args[1]), args[2])
    elif command == "delete" and len(args) == 2:
        delete_task(parse_id(args[1]))
    elif command == "mark-in-progress" and len(args) == 2:
        mark_task(parse_id(args[1]), "in-progress")
    elif command == "mark-done" and len(args) == 2:
        mark_task(parse_id(args[1]), "done")
    elif command == "list" and len(args) in (1, 2):
        list_tasks(args[1] if len(args) == 2 else None)
    else:
        print("Error: Invalid command or wrong number of arguments.\n")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()