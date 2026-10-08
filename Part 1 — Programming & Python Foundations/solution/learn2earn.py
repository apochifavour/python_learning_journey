resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 10},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

def list_resources():
    for resource in resources:
        print(resource)

def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None

def add_resource():
    resource_id = input("Resource ID: ").strip().upper()

    if find_resource(resource_id):
        print("Resource ID already exists.")
        return

    name = input("Resource name: ")
    category = input("Category: ")
    total = int(input("Total units: "))

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(resource)
    print("Resource added.")

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

borrow_records = []

def find_borrow(fellow_id, resource_id):
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            return record
    return None


def return_resource():
    fellow_id = input("Fellow ID: ").strip().upper()
    resource_id = input("Resource ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Fellow not found.")
        return


def borrow_resource():
    fellow_id = input("Fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Fellow not found.")
        return

    resource_id = input("Resource ID: ").strip().upper()  
    resource = find_resource(resource_id)
    if resource is None:
        print("Resource not found.")
        return
    try:    
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Enter a whole number.")
        return    
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    if quantity > resource["available"]:
        print("Not enough stock.")
        return 
    resource["available"] -= quantity 
    borrow_records.append({
    "fellow_id": fellow_id,
    "resource_id": resource_id,
    "quantity": quantity
}) 
    print("Borrowing successful.")

borrow_resource()         