names = ["H", "I", "M", "O", "N"]
age = [10, 11, 12, 13, 14]

# Print names and their corresponding ages
for i in range(len(names)):
    print(names[i], ":", age[i])

shoppingCart = ["Apple", "Banana", "Mango", "Jackfruit"]
print("List Total Element:", len(shoppingCart))

# Uncomment these lines to add items from user input
# item = input("Enter item name: ")
# shoppingCart.append(item)
# item = input("Enter your item: ")
# shoppingCart.append(item)

print("Items are:", shoppingCart)

# Remove element by value
shoppingCart.remove("Apple")
print("Items are:", shoppingCart)

# Remove the last item
shoppingCart.pop()
print("Items are:", shoppingCart)

# Remove element by index using del
del shoppingCart[0]  # Removing the first element
print("Items are after del:", shoppingCart)

# Remove element by index using pop
if shoppingCart:
    shoppingCart.pop(0)  # Removing the first element again if it exists
print("Items are after pop by index:", shoppingCart)

# Clear the list
shoppingCart.clear()
if len(shoppingCart) == 0:
    print("List is empty")

# Nested list
number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = len(number)
print("Nested list:", number)
print("Total Nested list items:",a)
print(number[2][1])

i=0
print("Nested list:")
while i < a:
    print(number[i])
    i += 1