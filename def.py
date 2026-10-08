transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def total_by_fellow(transactions):
    totals = {}

    for transaction in transactions:
        fellow = transaction["fellow"]
        quantity = transaction["quantity"]
        totals[fellow] = totals.get(fellow, 0) + quantity

    return totals

print(total_by_fellow(transactions))