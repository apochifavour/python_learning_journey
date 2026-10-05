first_name = "Chris"
last_name = "Ene"

full_name = first_name + " " + last_name
print(full_name)

name = "Ada"
print(name.upper())
Name = "ADA"
print(name.lower())

name = "chris ebute"
print(name.title())

name = "  Chris  "
print(name.strip())
name = input("Enter your name: ").strip()

message = "Hello Chris"
new_message = message.replace("Chris", "David")
print(new_message)

message = "Welcome to python"
position = message.find("Python")
print(position)

text = "banana"
print(text.count("a"))

product = "Keyboard"
print(product.startswith("Key"))

filename = "receipt.txt"
print(filename.endswith(".txt"))

name = input("Enter your name: ").strip()
print(f"Welcome, {name}!")

name = input("Enter your name: ").strip().title()
print(f"Welcome, {name}!")

print("======================")
print("     STORE RECEIPT")
print("======================")

customer = input("Enter customer name: ").strip().title()
product = input("enter product name: ").strip().title()

print(f"Customer: {customer}")
print(f"Product: {product}")


