import psycopg2
import psycopg2.extras

# TODO: consider security issues

HOST = "127.0.0.1"
USER = "postgres"
PASSWORD = "password"
DATABASE = "cd4ml"


class PostgresReader:
    def __init__(self):
        self.conn = None
        self.dbname = DATABASE
        self.user = USER
        self.password = PASSWORD
        self.host = HOST

    def _connect(self):
        self.conn = psycopg2.connect(dbname=self.dbname,
                                     user=self.user,
                                     password=self.password,
                                     host=self.host)

    def _query(self, sql_query):
        if self.conn is None:
            self._connect()

        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(sql_query)
        return cursor

    def _raw_data_query(self):
        table_name = "raw_data"
        sql_query = "SELECT * FROM {0}".format(table_name)
        return self._query(sql_query)

    def stream_data(self):
        for row in self._raw_data_query():
            yield row

        self.conn.close()
