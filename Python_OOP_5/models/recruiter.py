from models.employee import Employee


class Recruiter(Employee):
    def __init__(self, full_name=None, email=None, phone=None, salary_day=None):
        super().__init__(full_name=full_name, email=email, phone=phone, salary_day=salary_day)
        self.hired_this_month = 0

    def __str__(self):
        return "Recruiter: "+self.full_name

    def work(self):
        m_line = super().work()
        return m_line[:-1]+" and start hiring"


print('entry recruiter')
