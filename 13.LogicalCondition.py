#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

salary=int(input("Enter salary: "))

if salary <= 300000:
    tax=0
elif salary >=300001 and salary <=600000:
    tax=5
elif salary >=600001 and salary <=900000:
    tax=10
elif salary >=900001 and salary <=1200000:
    tax=15
elif salary >=1200001 and salary <=1500000:
    tax=20
else:
    tax=30
print("Income tax: ₹", tax)