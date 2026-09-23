price = 2500
quantity = 6
discount = 2000

subtotal = price * quantity
print(subtotal)
final_total = subtotal - discount
print(final_total)
# and
balance = 0
is_active = True
print(balance > 0 and is_active)
# or
is_admin = False
is_owner = True
print(is_admin or is_owner)
#not
is_logged_in = True
print(not is_logged_in)

balance = 50000
is_active = True
print(balance > 0 and is_active)

balance = 5000

if balance == 5000:
    print(balance)


balance = 50000
deposit = 20000
withdrawal = 15000

balance_after_deposit = balance + deposit
print(balance_after_deposit)
final_balance = balance_after_deposit - withdrawal
print(final_balance)

price = 7500
quantity = 6

total = price * quantity
print(total)

balance = 75000
deposit = 25000
withdrawal = 30000
new_balance = (balance + deposit) - withdrawal
print(new_balance)

# store order
price = 12000
quantity = 5
total = price * quantity
print(total)
total = 60000
quantity = 5
print(total >= 50000)
print(quantity > 0)
print(quantity < 10)

total = 30000
is_member = True
print(total >= 50000 or is_member)

# wallet app
starting_balance = 60000
deposit = 2000
balance = starting_balance + deposit
print(balance)
withdrawal = 10000
final_balance = balance - withdrawal
print(final_balance)

# store app
product = "Notebook"
price = 2000
quantity = 6
is_member = True

subtotal = price * quantity
print(subtotal >= 50000 or is_member)
print(product)
print(price)
print(quantity)
print(subtotal)
print(is_member)

balance = 40000
deposit = 10000
withdrawal = 15000

balance += deposit
balance -= withdrawal

is_positive = balance > 0