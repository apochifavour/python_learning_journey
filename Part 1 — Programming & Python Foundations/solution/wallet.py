print("===============")
print("   WALLET APP")
print("===============")

name = input("Enter your name: ")
balance = int(input("Enter current balance: "))
deposit = int(input("Enter deposit amount: "))

new_balance = balance + deposit

print()
print(f"Name: {name}")
print(f"Previous balance: \u20A6{balance}")
print(f"Deposit: \u20A6{deposit}")
print(f"New balance: \u20A6{new_balance}")