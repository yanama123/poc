import mysql.connector
from mysql.connector import errorcode


class TestDatabase:

    def __init__(self):

        self.DB_NAME = 'test_db'
        self.TABLE_NAME = 'prod2'
        self.TABLES = {'test_result': (
            "CREATE TABLE {} ("
            "  `id` varchar(255) NOT NULL,"
            "  `environment` TEXT NOT NULL,"
            "  `test` TEXT NOT NULL,"
            "  `created_at` TEXT NOT NULL,"
            "  `started_at` TEXT NOT NULL,"
            "  `finished_at` TEXT NOT NULL,"
            "  `status` TEXT NOT NULL,"
            "  `logs` TEXT NOT NULL)"
            "ENGINE=InnoDB").format(self.TABLE_NAME)}
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="adminadmin",
            database='test_db'
        )
        self.cursor = self.mydb.cursor(buffered=True)

        try:
            self.cursor.execute("USE {}".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(self.DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(self.cursor)
                print("Database {} created successfully.".format(self.DB_NAME))
                self.mydb.database = self.DB_NAME
            else:
                print(err)
        print('-------------------------')
        # print(self.TABLES)
        for table_name in self.TABLES:
            table_description = self.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                print('came here', err.errno, errorcode.ER_TABLE_EXISTS_ERROR)
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                    self.cursor.execute("USE test_db")
                else:
                    print(err.msg)
            else:
                print("OK")

    def show_table(self):
        self.cursor.execute("SHOW TABLES")
        for i in self.cursor:
            print(i)

    def show_all_data(self):
        self.cursor.execute("SELECT * from {}".format(self.TABLE_NAME))
        for i in self.cursor:
            print(i)
    def create_database(self, cursor):
        """

        :param cursor:
        :return:
        """

        try:
            cursor.execute(
                "CREATE DATABASE IF NOT EXIST {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    def insert_into_table(self, id, environment, test, created_at, started_at, finished_at, status, logs):
        """

        :param id: test_case_id
        :param environment: environment variable where test runs
        :param test: test_description
        :param created_at: test_creation_time
        :param started_at: test_started_time
        :param finished_at: test_finished_time
        :param status: test_status
        :param logs: test_logs
        :return:
        """

        self.cursor.execute("SHOW TABLES")
        add_results = ("INSERT INTO {}"
                       "(id, environment, test, created_at, started_at, finished_at, status, logs)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)").format(self.TABLE_NAME)
        data = (id, environment, test, created_at,
                started_at, finished_at, status, logs)
        self.cursor.execute(add_results, data)
        self.mydb.commit()

    def update_into_table(self,  id, finished_at, status, logs):
        """

        :param id:
        :param finished_at:
        :param status:
        :param logs:
        :return:
        """
        # prepare query and data
        query = """ UPDATE {}
                    SET finished_at = %s, status = %s, logs = %s
                    WHERE id = %s """.format(self.TABLE_NAME)

        data = (finished_at, status, logs, id)
        self.cursor.execute(query, data)

        # accept the changes
        self.mydb.commit()


    def display(self):
        """

        :return: result which contains id, status, logs
        """
        """

        :return:
        """
        print('table name', self.TABLE_NAME)
        self.cursor.execute("SELECT id, status, logs FROM {}".format(self.TABLE_NAME))

        result = self.cursor.fetchone()
        return result

    def status_from_id(self, id):
        """

        :param id: test_case_id
        :return:
        """
        print('table', self.TABLE_NAME)
        print('cametoid', type(id[0]))
        self.cursor.execute('SELECT status, logs FROM {} WHERE id = "{}"'.format(self.TABLE_NAME, id[0]))
        print('cursor', self.cursor)
        status_from_id = self.cursor.fetchall()
        print('s', status_from_id)
        return status_from_id


#For testing

# tes = TestDatabase()
# tes.show_table()
# tes.show_all_data()
# # print(tes)
# tes.insert_into_table('Gna', '20006381', 'kana', 'ham', '3000', 'a', 'b', 'c')
# tes.update_into_table('Gna', 'hammmeracd', 'finished', 'log ceated successfully')
# print('111111111111111111111111111111')
# tes.display()
# tes.status_from_id(['test_files/test_shell_scripts.bats'])

