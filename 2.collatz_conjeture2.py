
'''
Same as above.
Input two numbers.
Print which number has less steps to reach 1.
'''

getNumber1=int(input("Enter a number1: "))
getNumber2=int(input("Enter a number2: "))

num1,num2=getNumber1,getNumber2

step1=0
step2=0

while num1!=1:
    if num1 % 2==0:
        num1 = (num1//2)
    else:
        num1 = 3* num1 + 1
    
    step1+=1

while num2!=1:
    if num2 % 2 == 0:
        num2 = (num2 //2)
    else:
        num2 = 3* num2 + 1
    step2+=1

if step1 < step2:
    print(f"{getNumber1} reach 1 is less steps")

elif step2 < step1:
    print(f"{getNumber2} reach 1 is less steps")

else:
    print(f"Both number reach 1 in same steps")

