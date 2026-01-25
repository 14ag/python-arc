import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################classroom grader########################################

honors_students=[]
students = [["Alice", 95], ["Bob", 78], ["Charlie", 92], ["David", 85]]
for student in students:
    if student[1] >=90:
        honors_students.append(student[0])

print(honors_students)