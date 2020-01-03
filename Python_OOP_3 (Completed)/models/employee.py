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
            days = 0
            for day in range(diff):
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


print('entry Employee')
