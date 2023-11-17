#3. Sort the numbers in an array (ascending or descending).
 #Write a function that finds the largest number in an array

numbers = [5, 2, 9, 1, 7]

# Sort in ascending order
sorted_numbers_ascending = sorted(numbers)
print("Sorted in ascending order:", sorted_numbers_ascending)

# Sort in descending order
sorted_numbers_descending = sorted(numbers, reverse=True)
print("Sorted in descending order:", sorted_numbers_descending)

# Find the largest number
largest_number = max(sorted_numbers_ascending)
print("Largest number in the array:", largest_number)