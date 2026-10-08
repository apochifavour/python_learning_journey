# Learn2Earn Equipment Lending System

resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


# =========================
# HELPER FUNCTIONS
# =========================

def find_resource(resource_id):
    """Find a resource by ID."""
    for resource in resources:
        if resource["id"].upper() == resource_id.upper():
            return resource

    return None


def get_borrow_record(fellow_id, resource_id):
    """Find a current borrowing record."""
    for record in borrow_records:
        if (
            record["fellow_id"].upper() == fellow_id.upper()
            and record["resource_id"].upper() == resource_id.upper()
        ):
            return record

    return None


def get_integer(prompt):
    """Get a valid integer from the user."""
    while True:
        value = input(prompt).strip()

        try:
            return int(value)
        except ValueError:
            print("Error: Please enter a valid integer.")


# =========================
# RESOURCE FUNCTIONS
# =========================

def add_resource():
    print("\n========== ADD RESOURCE ==========")

    resource_id = input("Resource ID: ").strip().upper()

    if find_resource(resource_id) is not None:
        print("Error: Resource ID already exists.")
        return

    name = input("Resource name: ").strip()
    category = input("Category: ").strip()

    if not name:
        print("Error: Resource name cannot be empty.")
        return

    if not category:
        print("Error: Category cannot be empty.")
        return

    total = get_integer("Total units: ")

    if total <= 0:
        print("Error: Total units must be greater than 0.")
        return

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(resource)

    print("Resource added successfully.")


def list_resources():
    print("\n========== RESOURCE INVENTORY ==========")

    if not resources:
        print("No resources available.")
        return

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']} | "
            f"Borrowed: {borrowed}"
        )


# =========================
# BORROWING
# =========================

def borrow_resource():
    print("\n========== BORROW RESOURCE ==========")

    fellow_id = input("Fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow not found.")
        return

    resource_id = input("Resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource not found.")
        return

    quantity = get_integer("Quantity: ")

    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return

    if quantity > resource["available"]:
        print(
            f"Error: Not enough stock available. "
            f"Only {resource['available']} unit(s) available."
        )
        return

    # Everything has been validated.
    # Only now do we modify the state.

    existing_record = get_borrow_record(fellow_id, resource_id)

    if existing_record is not None:
        existing_record["quantity"] += quantity
    else:
        borrow_records.append(
            {
                "fellow_id": fellow_id,
                "resource_id": resource_id,
                "quantity": quantity
            }
        )

    resource["available"] -= quantity

    print(
        f"Borrowing successful: "
        f"{fellows[fellow_id]} borrowed {quantity} "
        f"{resource['name']}(s)."
    )


# =========================
# RETURNS
# =========================

def return_resource():
    print("\n========== RETURN RESOURCE ==========")

    fellow_id = input("Fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow not found.")
        return

    resource_id = input("Resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource not found.")
        return

    quantity = get_integer("Quantity: ")

    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return

    record = get_borrow_record(fellow_id, resource_id)

    if record is None:
        print("Error: This fellow currently has no loan for this resource.")
        return

    if quantity > record["quantity"]:
        print(
            f"Error: Return quantity exceeds current loan. "
            f"Current loan: {record['quantity']}."
        )
        return

    # Everything has been validated.
    # Now update the borrowing record and inventory.

    record["quantity"] -= quantity
    resource["available"] += quantity

    # Remove the record if nothing remains on loan.
    if record["quantity"] == 0:
        borrow_records.remove(record)

    print(
        f"Return successful: "
        f"{fellows[fellow_id]} returned {quantity} "
        f"{resource['name']}(s)."
    )


# =========================
# SEARCH
# =========================

def search_resources():
    print("\n========== SEARCH RESOURCES ==========")

    search_term = input("Enter resource name: ").strip().lower()

    if not search_term:
        print("Error: Search term cannot be empty.")
        return

    found = False

    for resource in resources:
        if search_term in resource["name"].lower():
            print(
                f"ID: {resource['id']} | "
                f"Name: {resource['name']} | "
                f"Category: {resource['category']} | "
                f"Available: {resource['available']}"
            )

            found = True

    if not found:
        print("No matching resources found.")


def filter_by_category():
    print("\n========== FILTER BY CATEGORY ==========")

    category = input("Enter category: ").strip().lower()

    if not category:
        print("Error: Category cannot be empty.")
        return

    found = False

    for resource in resources:
        if resource["category"].lower() == category:
            print(
                f"ID: {resource['id']} | "
                f"Name: {resource['name']} | "
                f"Category: {resource['category']} | "
                f"Available: {resource['available']}"
            )

            found = True

    if not found:
        print("No resources found in that category.")


# =========================
# REPORT
# =========================

def generate_report():
    print("\n========== REPORT ==========")

    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Borrowed units: {borrowed_units}")

    # Low-stock resources
    print("\nLow stock:")

    low_stock_found = False

    for resource in resources:
        if resource["available"] < 3:
            print(
                f"- {resource['name']} "
                f"({resource['available']} available)"
            )
            low_stock_found = True

    if not low_stock_found:
        print("- None")

    # Find highest number currently borrowed
    highest_borrowed = 0

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed > highest_borrowed:
            highest_borrowed = borrowed

    print("\nMost borrowed:")

    if highest_borrowed == 0:
        print("- None")
    else:
        for resource in resources:
            borrowed = resource["total"] - resource["available"]

            if borrowed == highest_borrowed:
                print(
                    f"- {resource['name']} "
                    f"({borrowed} currently borrowed)"
                )

    print("============================")


# =========================
# BORROWING RECORDS
# =========================

def show_borrow_records():
    print("\n========== CURRENT BORROWING RECORDS ==========")

    if not borrow_records:
        print("No active borrowing records.")
        return

    for record in borrow_records:
        fellow_name = fellows[record["fellow_id"]]
        resource = find_resource(record["resource_id"])

        print(
            f"Fellow: {record['fellow_id']} - {fellow_name} | "
            f"Resource: {resource['name']} | "
            f"Quantity: {record['quantity']}"
        )


# =========================
# MENU
# =========================

def show_menu():
    print("\n")
    print("==========================================")
    print("     LEARN2EARN EQUIPMENT LENDING")
    print("==========================================")
    print("1. Add Resource")
    print("2. List Resources")
    print("3. Borrow Resource")
    print("4. Return Resource")
    print("5. Search Resource")
    print("6. Filter by Category")
    print("7. Generate Report")
    print("8. Show Borrowing Records")
    print("9. Exit")
    print("==========================================")


# =========================
# MAIN PROGRAM
# =========================

def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            show_borrow_records()

        elif choice == "9":
            print("Thank you for using Learn2Earn Equipment Lending.")
            break

        else:
            print("Error: Invalid menu option. Please choose 1-9.")


# Start the application
if __name__ == "__main__":
    main()