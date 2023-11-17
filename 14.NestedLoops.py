# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

num_students = 3
num_marks = 2

for student in range(1, num_students + 1):
    student_name = input(f"Enter the name of Student {student}: ")
    for mark in range(1, num_marks + 1):
        input_mark = float(input(f"Enter Mark {mark} for {student_name}: "))
        print(f"Mark {mark} for {student_name} is {input_mark}")


