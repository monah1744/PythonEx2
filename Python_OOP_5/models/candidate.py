from models.employee import Employee


class UnableToWorkException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class Candidate(Employee):
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        super().__init__(full_name=full_name, email=email, phone="050", salary_day=0)
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @classmethod
    def from_csv_file(cls, file_name):
        pass

    def work(self):
        raise UnableToWorkException("It can't work")
