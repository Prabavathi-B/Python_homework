#4. THere are two arrays of numbers. the numbers are sorted in ascending order. 
#Find the numbers that are common in both arrays. 
#Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]

array1 = [9, 7, 3, 1, 14, 13]
array2 = [7, 2, 15, 1, 13]

ascending1 = sorted(array1)
ascending2 = sorted(array2)

print("The ascending order array1 and array2:", ascending1, ascending2)

# Find common elements
common_elements = []

for i in ascending1:
    if i in ascending2:
        common_elements.append(i)   

print("Common elements:", common_elements)





