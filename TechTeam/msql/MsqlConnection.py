import mysql.connector


class MsqlConnection(object):

    def __init__(self):
        self._create_conn()

    def _create_conn(self):
        HOST = '80.211.191.58'
        DB = 'supportsystem'
        USER = 'adrian'
        PASS = 'Privado1'

        self.connection = mysql.connector.connect(host=HOST, database=DB, user=USER, password=PASS)
        self.cursor = self.connection.cursor()

    def execute(self, sentence):
        self.cursor.execute(sentence)

    def get_one(self, sentence):
        self.cursor.execute(sentence)
        return self.cursor.fetchone()

    def get_all(self, sentence):
        self.cursor.execute(sentence)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
