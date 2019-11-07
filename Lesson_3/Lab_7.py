import random

students = ['Vasya', 'Kolya', 'Petya', 'Masha', 'Platon']
stud_dict = {}

students.sort()
for student in students:
    # print(student)
    stud_dict[student] = []
    for _ in range(10):
        stud_dict[student].append(random.randint(1, 5))
print(stud_dict)
for student in stud_dict:
    print("Student {name} has average mark {mark}".format(
        name=student,
        mark=sum(stud_dict.get(student))/len(stud_dict.get(student))
    ))
    for i in stud_dict.get(student):
        print(i, end=" ")
    print()
