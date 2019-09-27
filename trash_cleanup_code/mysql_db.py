import sqlite3
import mysql.connector


class TestsDatabase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="adminadmin",
        )
        self.mycursor = self.mydb.cursor(buffered=True)
        self.mycursor.execute("SHOW DATABASES")
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS project_db")

        # use database
        self.mycursor.execute("""USE project_db""")
        try:
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS testresults (name VARCHAR(255),"
                                  "                id text PRIMARY KEY,"
                                  "environment text,"
                                  "test text,"
                                  "created_at text,"
                                  "started_at text,"
                                  "finished_at text,"
                                  "status text,"
                                  "logs text"
                                  )
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def add_test_results(self, id, environment, test, crated_at, started_at, finished_at, status, logs):
        """

        :param id:
        :param environment:
        :param test:
        :param crated_at:
        :param started_at:
        :param finished_at:
        :param status:
        :param logs:
        :return:
        """
        self.id = id
        self.environment = environment
        self.test = test
        self.created_at = crated_at
        self.started_at = started_at
        self.finished_at = finished_at
        self.status = status
        self.logs = logs

        try:
            self.mycursor.execute("INSERT INTO testresults VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )"
                           .format(self.id, self.environment, self.test, self.created_at,
                                   self.started_at, self.finished_at, self.status, self.logs))
        except sqlite3.IntegrityError as e:
            print("Failed to Insert the element due to - {}".format(e))
        self.mydb.commit()

    def update_test_results(self, id, finished_at, status, logs):
        """

        :param id:
        :param finished_at:
        :param status:
        :param logs:
        :return:
        """
        try:
            self.mycursor.execute(
                "UPDATE testresults SET finished_at='{}',status='{}',logs='{}' WHERE id='{}'".format(finished_at,
                                                                                                     status, logs, id))
            self.mydb.commit()
        except Exception as e:
            print(e.message)

    def get_status(self, id):
        # self.conn = sqlite3.connect('results.db')
        # # self.conn = sqlite3.connect(':memory:')
        # self.c = self.conn.cursor()
        print('id', id[0])
        rows = self.mycursor.execute('SELECT status FROM testresults WHERE id ="{}"'.format(id[0])).fetchall()
        for row in rows:
            print(row)
        return row

    def display(self):
        """

        :return:
        """
        result = self.mycursor.execute("""SELECT * FROM testresults""").fetchall()
        print(result)
        return result


if __name__ == '__main__':
    emp = TestsDatabase()
    id = 'Anji'
    # emp.get_status(id)

    emp.add_test_results('GaAnji', 20006381, 'RealProtect', 'Sham', '3000', 'a', 'b', 'c')
    emp.display()
#     emp.select_task_by_priority('GaAnji')
#     # emp.display()
