from datetime import date, timedelta


class Employee:
    def __init__(self, full_name=None, email=None, phone=None, salary_day=None):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.salary_day = salary_day

    def work(self):
        return ("I come to the office.")

    def check_salary(self, days=None):
        if days is (None):
            now = date.today()
            month_start = date(now.year, now.month, 1)
            weekend = [5, 6]
            diff = (now - month_start).days + 1
            # print(now, month_start, diff)
            days = 0
            for day in range(diff):
                # print((month_start + timedelta(day)).weekday())
                if (month_start + timedelta(day)).weekday() not in weekend:
                    days += 1
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
    def __init__(self, full_name=None, email=None, phone=None, salary_day=None):
        super().__init__(full_name=full_name, email=email, phone=phone, salary_day=salary_day)
        self.hired_this_month = 0

    def __str__(self):
        return "Recruiter: "+self.full_name

    def work(self):
        m_line = super().work()
        return m_line[:-1]+" and start hiring"


class Programmer(Employee):
    def __init__(self, full_name=None, email=None, phone=None, salary_day=None):
        super().__init__(full_name=full_name, email=email, phone=phone, salary_day=salary_day)
        self.tech_stack = []
        self.closed_this_month = []

    def __str__(self):
        return "Programmer: "+self.full_name

    def work(self):
        m_line = super().work()
        return m_line[:-1]+" and start coding"

    def __lt__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) < len(other.tech_stack)
        else:
            return self.salary_day < other.salary_day

    def __gt__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) > len(other.tech_stack)
        else:
            return self.salary_day > other.salary_day

    def __eq__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) == len(other.tech_stack)
        else:
            return self.salary_day == other.salary_day

    def __le__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) <= len(other.tech_stack)
        else:
            return self.salary_day <= other.salary_day

    def __ge__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) >= len(other.tech_stack)
        else:
            return self.salary_day >= other.salary_day

    def __neq__(self, other):
        if isinstance(other, Programmer):
            return len(self.tech_stack) != len(other.tech_stack)
        else:
            return self.salary_day != other.salary_day

    def __add__(self, other):
        total_salary = self.salary_day + other.salary_day
        total_P = Programmer(self.full_name, self.email,
                             self.phone, total_salary)
        total_P.tech_stack = self.tech_stack + other.tech_stack
        return total_P


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
