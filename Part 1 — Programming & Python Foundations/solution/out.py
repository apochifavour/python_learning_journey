name = "chris"
balance = 15000

print(name, balance)

name = "Chris"
balance = 15000

print(f"Hello {name}")
print(f"Your balance is ₦{balance}")

price = 2000
quantity = 4

print(f"Total: ₦{price * quantity}")


print("=== WALLET DEPOSIT ===")

balance = float(input("Enter current balance: ₦"))
deposit = float(input("Enter deposit amount: ₦"))

new_balance = balance + deposit

print()
print("Deposit successful!")
print(f"Previous balance: ₦{balance}")
print(f"Deposit: ₦{deposit}")
print(f"New balance: ₦{new_balance}")