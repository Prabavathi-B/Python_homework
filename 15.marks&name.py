#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67

num_students = 3
num_marks = 2

for student in range(1, num_students + 1):
    student_name = input(f"Enter the name of Student {student}: ")
    marks = []
    for mark in range(1, num_marks + 1):
        input_mark = float(input(f"Enter Mark {mark} for {student_name}: "))
        marks.append(input_mark)
    print(f"{student_name}'s marks {', '.join(map(str, marks))}")