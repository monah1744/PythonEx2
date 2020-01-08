from models.employee import Employee


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


print('entry programmer')
