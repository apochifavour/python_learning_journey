import json
from pathlib import Path

FILE = Path(__file__).with_name("tickets.json")


def load_tickets():
    if FILE.exists() and FILE.read_text().strip():
        return json.loads(FILE.read_text())
    return []


def save_tickets(tickets):
    FILE.write_text(json.dumps(tickets, indent=2))


def create():
    title = input("Title: ").strip()
    priority = input("Priority (low/medium/high): ").strip().lower()
    users = input("Affected users: ").strip()
    if not title or priority not in ("low", "medium", "high") or not users.isdigit():
        return print("Invalid input.")
    tickets = load_tickets()
    new_id = max((t["id"] for t in tickets), default=0) + 1
    tickets.append({"id": new_id, "title": title, "priority": priority,
                    "affected_users": int(users), "status": "open", "assigned_to": None})
    save_tickets(tickets)
    print(f"Ticket #{new_id} created.")


def get_ticket(tickets):
    ticket_id = input("Ticket id: ").strip()
    return next((t for t in tickets if str(t["id"]) == ticket_id), None)


def assign():
    tickets = load_tickets()
    ticket = get_ticket(tickets)
    if not ticket:
        return print("Ticket not found.")
    ticket["assigned_to"] = input("Staff name: ").strip()
    ticket["status"] = "in_progress"
    save_tickets(tickets)
    print("Assigned.")


def find():
    print(get_ticket(load_tickets()) or "Ticket not found.")


ACTIONS = {"1": create, "2": assign, "3": find}

while True:
    print("\n" + "=" * 30 + "\n" + "CampusFlow".center(30) + "\n" + "=" * 30)
    print("1. Create  2. Assign  3. Find  4. Quit")
    choice = input("Choose: ").strip()
    if choice == "4":
        break
    ACTIONS.get(choice, lambda: print("Invalid choice."))()