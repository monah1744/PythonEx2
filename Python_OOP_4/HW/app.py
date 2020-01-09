from db_query import Dbquery
from models.candidate import Candidate
from models.programmer import Programmer
from models.recruiter import Recruiter
from models.vacancy import Vacancy


def prepare_tables(dbname, user, password, host):
    table_programmer = """CREATE TABLE IF NOT EXISTS programmer(id_programmer serial,
                                                              first_name varchar(48),
                                                              last_name varchar(48),
                                                              email varchar(48),
                                                              hired_at date,
                                                              phone varchar(20),
                                                              salary_per_day INTEGER,
                                                              main_skill varchar(48)
                                                              );
    """
    table_recruiter = """CREATE TABLE IF NOT EXISTS recruiter(id_recruiter serial,
                                                            first_name varchar(48),
                                                            last_name varchar(48),
                                                            email varchar(48),
                                                            hired_at date,
                                                            phone varchar(20),
                                                            salary_per_day INTEGER
                                                            );
    """
    table_candidate = """CREATE TABLE IF NOT EXISTS candidate(id_candidate serial,
                                                            first_name varchar(48),
                                                            last_name varchar(48),
                                                            email varchar(48),
                                                            hired_at date,
                                                            phone varchar(20),
                                                            main_skill varchar(48)
                                                            );
    """
    table_vacancy = """CREATE TABLE IF NOT EXISTS vacancy(id_candidate serial,
                                                        title varchar(48),
                                                        salary INTEGER,
                                                        main_skill varchar(48),
                                                        technologies text,
                                                        id_recruiter INTEGER,
                                                        hired_candidate BOOLEAN,
                                                        status BOOLEAN
                                                        );
    """
    table_interview = """CREATE TABLE IF NOT EXISTS interview(id_interview serial,
                                                            id_vacancy INTEGER,
                                                            id_programmer INTEGER,
                                                            id_recruiter INTEGER,
                                                            id_candidate INTEGER,
                                                            datetime timestamp,
                                                            feedback text,
                                                            result BOOLEAN
                                                            );
    """
    my_query = Dbquery(dbname, user, password, host)
    my_query.execute_table(table_programmer)
    my_query.execute_table(table_recruiter)
    my_query.execute_table(table_candidate)
    my_query.execute_table(table_vacancy)
    my_query.execute_table(table_interview)
    del my_query


def main():
    db_name = 'inovikov'
    db_user = 'inovikov'
    db_password = 'inovikov'
    db_host = '127.0.0.1'

    prepare_tables(db_name, db_user, db_password, db_host)

    test_programmer = Programmer(
        full_name="Ivan Novikov", email="inovikov@example.com", phone="+380502255677",
        salary_day=20, hired_at="2019-12-28", main_skill="Python")
    my_query = Dbquery(db_name, db_user, db_password,
                       db_host, table_name="programmer")
    my_query.create(test_programmer)
    pass


if __name__ == "__main__":
    main()
