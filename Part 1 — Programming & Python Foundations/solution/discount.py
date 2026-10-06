customer_name = input("Enter customer name: ")
purchase_total = float(input("Enter purchase total: "))

if purchase_total >= 100000:
    discount = purchase_total * 0.20
elif purchase_total >= 50000:
    discount = purchase_total * 0.10
else:
    discount = 0

final_total = purchase_total - discount

print("==============================")
print("       STORE CHECKOUT")
print("==============================")

print("Customer:", customer_name)
print("Original total: ₦" + str(purchase_total))
print("Discount: ₦" + str(discount))
print("Final total: ₦" + str(final_total))

print("==============================")