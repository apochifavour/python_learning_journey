balance = 3000
Withdrawal = 1000
if balance >= Withdrawal:
    print("Withdrawal approved")
else:
    print("Insuficient balance")

is_student = True

print(is_student)


age = 20

if age >= 18:
    print("You are an adult")


if balance >= 5000:
    print("You can make the purchase")
else:
    print("Insufficient balance")



balance = float(input("Enter balance: ₦"))
withdrawal = float(input("Enter withdrawal amount: ₦"))

if balance >= withdrawal:
    balance = balance - withdrawal
    print(f"Withdrawal approved.")
    print(f"Remaining balance: ₦{balance}")
else:
    print("Insufficient balance.") 


score = 40
if score >= 70:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")

age = 30

if age >= 18 and age <= 60:
    print("Age is within the range")


balance = 10000
withdrawal = 5000

if balance > 0:
    if withdrawal <= balance:
        print("Withdrawal approved")


age = 30

if age >= 18 and age <= 60:
    print("Age is within the range")

balance = 20000
has_wallet = True
price = 2000

if has_wallet:
    if balance >= price:
        print("Purchase approved")

has_wallet = True

if has_wallet:
    print("Wallet found")

name = "Chris"

if name == "Chris":
    print("Welcome Chris")

password = "python123"

if password == "python123":
    print("Login successful")

username = input("Username: ").strip().lower()

if username == "admin":
    print("Welcome, administrator.")
else:
    print("Unknown user.") 

total = 200
if total >= 20000:
    print("Free delivery")
else:
    print("Delivery fee applies")


