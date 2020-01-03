from models.candidate import Candidate
from models.programmer import Programmer
from models.recruiter import Recruiter
from models.vacancy import Vacancy

first_P = Programmer("Ivan Novikov", "email1@gmail.com", "050", 30)
first_P.tech_stack = ["Python", "C++"]

second_P = Programmer("Ivan Ne_novikov", "email3@gmail.com", "050", 50)
second_P.tech_stack.append("PHP")

first_R = Recruiter("Marina Laktionova", "email2@gmail.com", "050", 20)

first_C = Candidate("Dmitriy Shmatko", "dshamtko@gmail.com", ["Lua", "Python", "Puppet"], ["Lua"], 10)
second_C = Candidate("Anatoliy Laktionov", "alaktionov@gmail.com", ["Lua", "Python", "Puppet"], ["Python"], 5)
third_C = Candidate("Igor Vnukov", "ivnukov@gmail.com", ["Lua", "Python", "PHP"], ["Python"], 10)

first_V = Vacancy("Middle Python", "Python", 5)
second_V = Vacancy("Senior Python", "Python", 8)
