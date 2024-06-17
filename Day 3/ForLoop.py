# Loop to print numbers from 0 to 4
for i in range(0, 5):
    print(i)  # Print the current number

# List of fruits
fruit = ["Apple", "Banana", "Mango", "Strawberry"]

# Loop to print each fruit in the list
for element in fruit:
    print(element)  # Print the current fruit

# List of numbers
a = [1, 3, 5, 7, 9]

# Loop to add 2 to each element in the list and print the result
for element in a:
    element += 2  # Add 2 to the current element
    print(element)  # Print the modified element

# Print the original list to show it remains unchanged
print(a)  # [1, 3, 5, 7, 9]

# Loop to add 2 to each element in the list and update the list
for i in range(0, len(a)):
    a[i] += 2  # Add 2 to the current element and update the list

# Print the modified list to show the changes
print(a)  # [3, 5, 7, 9, 11]
