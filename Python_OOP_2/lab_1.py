class Employee:
    def __init__(self, full_name=None, phone=None, salary_day=None):
        self.full_name = full_name
        self.phone = phone
        self.salary_day = salary_day

    def work(self):
        return ("I come to the office.")

    def check_salary(self, days):
        return self.salary_day*days

    def __lt__(self, other):
        return self.salary_day < other.salary_day

    def __gt__(self, other):
        return self.salary_day > other.salary_day

    def __eq__(self, other):
        return self.salary_day == other.salary_day

    def __le__(self, other):
        return self.salary_day <= other.salary_day

    def __ge__(self, other):
        return self.salary_day >= other.salary_day

    def __neq__(self, other):
        return self.salary_day != other.salary_day


class Recruiter(Employee):
    def __str__(self):
        return "Recruiter: "+self.full_name

    def work(self):
        m_line = super().work()
        return m_line[:-1]+" and start hiring"


class Programmer(Employee):
    def __str__(self):
        return "Programmer: "+self.full_name

    def work(self):
        m_line = super().work()
        return m_line[:-1]+" and start coding"


a = Programmer("Ivan Novikov", "050", 30)
print(a)
print(a.work())

b = Recruiter("Ivan Novikov", "050", 20)
print(b)
print(b.work())

if a < b:
    print('OK')
else:
    print('not OK')
if a > b:
    print('OK')
else:
    print('not OK')
