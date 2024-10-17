
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
favorite_foods = ['pizza','chicken','beef', 'grilledchicken','fish','liver']
favorite_foods.append("juice")
favorite_foods.append("yorgut")
favorite_foods.remove("fish")
print(favorite_foods)
#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
numbers = [2,5,8,10,3,6]
print("First element:",numbers[0])
print("Last element:",numbers[-1])
print("Reversed:",numbers[::-1])
total_sum = sum(numbers)
print("sum of all elements:",total_sum)