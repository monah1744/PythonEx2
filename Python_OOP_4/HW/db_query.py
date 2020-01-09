import psycopg2


class Dbquery:
    def __init__(self, dbname, user, password, host="127.0.0.1",  port="5432", table_name=None):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        if table_name is not None:
            self.table_name = table_name

    def set_tablename(table_name):
        self.table_name = table_name

    def create(self, temp_obj):
        if self.table_name is None:
            raise ValueError("test error")
        query_line = f"""INSERT INTO {self.table_name} """
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def read(self):
        pass

    def execute_table(self, query):
        conn = psycopg2.connect(database=self.dbname, user=self.user,
                                password=self.password, host=self.host, port=self.port)
        # print("Database opened successfully")
        cursor = conn.cursor()
        cursor.execute(query)
        # print("Table created successfully")
        conn.commit()
        conn.close()


def main():
    pass


if __name__ == "__main__":
    main()
