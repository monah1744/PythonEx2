import sys
from models.recruiter import Recruiter
from models.programmer import Programmer

a = Programmer("Ivan Novikov", "email1@gmail.com", "050", 30)
print(a)
print(a.work())
a.tech_stack = ["test1", "test3"]
print(a.tech_stack)

c = Programmer("Ivan Novikov", "email3@gmail.com", "050", 50)
print(c)
print(c.work())
c.tech_stack.append("test2")

b = Recruiter("Ivan Novikov", "email2@gmail.com", "050", 20)
print(b)
print(b.work())

if a < c:
    print('OK')
else:
    print('not OK')
if a > c:
    print('OK')
else:
    print('not OK')


if a < b:
    print('OK')
else:
    print('not OK')
if b < a:
    print('OK')
else:
    print('not OK')

print(a.check_salary(10))
print(a.check_salary())
print(b.check_salary(10))
print(b.check_salary())
z = a+c
print(z.tech_stack)
print(z)
