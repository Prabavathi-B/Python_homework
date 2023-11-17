
'''
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.
'''

num=int(input("Enter a number: "))

while num!=1  and num!=0:
    if num % 2==0:
        num = (num//2)
    else:
        num = 3*num+1
    
    print(num)