balance = 30000
withdrawal = 8000

balance_after_withdrawal = balance - withdrawal
print(balance_after_withdrawal)

result = 10 / 2
print(result)
print(type(result))

print(10 + 5)
print(20 - 8)
print(6 * 7)
print(20 / 4)

# floor division
items = 17
boxes = 5
full_boxes = items // boxes
print(full_boxes)

# modulo
number = 10
remainder = number % 2
print(remainder)

# Case 1
total = 60000
is_member = False
print(total >= 50000 or is_member)   # True

# Case 2
total = 30000
is_member = True
print(total >= 50000 or is_member)   # True

# Case 3
total = 30000
is_member = False
print(total >= 50000 or is_member)   # False

balance = 10000
withdrawal = 20000
is_active = True

print(balance <= withdrawal and is_active)