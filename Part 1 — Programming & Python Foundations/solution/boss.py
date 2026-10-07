account_name = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal")

elif withdrawal > balance:
    print("Insufficient balance")

else:
    remaining_balance = balance - withdrawal

    print("Approved")
    print("Account Holder:", account_name)
    print("Remaining:", remaining_balance)