import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self):
        self.path = "markt_pilot.sqlite.db"

    def create_table(self,sql):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by self.path
        :return: Connection object or None
        """
        connection = None
        try:
            connection = sqlite3.connect(self.path)
        except Error as e:
            print(e)

        return connection