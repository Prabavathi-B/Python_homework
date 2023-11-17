'''
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their 
mark in the format name:mark.
Also print the number of students who failed.
'''

studName = ['anandhi', 'kabila', 'kavitha', 'devika', 'praba']
csMark = [90, 67, 89, 30, 45]

passMark = 50

passedStudents = []
failedStudents = []


for student in range(len(studName)):
    name = studName[student]
    mark = csMark[student]
    if mark >= passMark:
        passedStudents.append(f"{name}: {mark}")
    else:
          failedStudents.append(f"{name}:{mark}")

for student in passedStudents:
    print(student)

print(f"Number of students who failed: {len(failedStudents)}")
for student in failedStudents:
    print(student)

