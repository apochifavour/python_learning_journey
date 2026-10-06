customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 100000:
    discount = subtotal * 0.20
elif subtotal >= 50000:
    discount = subtotal * 0.10
else:
    discount = 0

final_total = subtotal - discount

print("================================")
print("         STORE RECEIPT")
print("================================")

print("Customer:", customer_name)
print("Product:", product_name)
print("Quantity:", quantity)
print("Subtotal: ₦" + str(subtotal))

print()
print("Discount: ₦" + str(discount))
print("Final Total: ₦" + str(final_total))

print("================================")