
'''
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function
'''
#get the input fron user for the first string and second string
first_string=input("enter the first string: ")
second_string=input("enter the second string: ")
#create a empty list to store the right shifted string
list_all_right_shifted_words_of_string=[]
#iterate the loop for right shifting condition
for sam in first_string:
    #use slice method to shifting the first char into last char
    first_string = first_string[1:] + first_string[0]
    #append the right shifted words
    list_all_right_shifted_words_of_string.append(first_string)

#if the second string is in the list then print 'first_string  is same as second_string'
if second_string in list_all_right_shifted_words_of_string:
    print(f"{first_string} is same as {second_string}")
#else print 'first_string  is not same as second_string'
else:
    print(f"{first_string} is not same as {second_string}")

