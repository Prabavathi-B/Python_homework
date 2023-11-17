
'''
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''


students_name_list=['devi','rani','praba','anandhi','kavi']
#assign the passmark
pass_mark=50

cs_mark_list=[45,97,97,89,90]
math_mark_list=[34,98,98,87,30] 
english_mark_list=[25,97,87,82,79]

for student_list in  range (len(students_name_list)):
    if (cs_mark_list[student_list] >= 90)  and (math_mark_list[student_list] >= 90) and (english_mark_list[student_list] >= 90):
        print(f"{students_name_list[student_list]} got A in all subjects")

    elif ((cs_mark_list[student_list] >= 90)  or (math_mark_list[student_list] >= 90) or (english_mark_list[student_list] >= 90)) and ((cs_mark_list[student_list] >= 80)  or (math_mark_list[student_list] >= 80) or (english_mark_list[student_list] >= 80)):
        print(f" {students_name_list[student_list]} got one A and the rest B. ")

    elif ((cs_mark_list[student_list] >= 80)  or (math_mark_list[student_list] >= 80) or (english_mark_list[student_list] >= 80)):
        print(f"{students_name_list[student_list]} got fail in all subjects")