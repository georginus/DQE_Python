import sqlite3


class DBConnection:
    def __init__(self, database_name='task09.db'):
        with sqlite3.connect(database_name) as self.connection:
            self.cur = self.connection.cursor()

    def createTableNews(self):
        self.cur.execute(
            'create table if not exists News (post_code integer, post_name text, post_text text, post_city text, post_date text)')

    def createTablePrivateAd(self):
        self.cur.execute(
            'create table if not exists PrivateAd (post_code integer, post_name text, post_text text, expiration_date text)')

    def createTableLifehack(self):
        self.cur.execute(
            'create table if not exists Lifehack (post_code integer, post_name text, post_text text, hashtag text, post_date text)')

    def select(self, table, columns):
        return self.cur.execute(f'select {columns} from {table}').fetchall()

    def insert(self, table, values):
        self.cur.execute(f"insert into {table} values ({values})")

    def closeCursor(self):
        self.cur.close()


dbcon = DBConnection()
# #
# # # dbcon.insert('people', "'Gavrila', 'Chichenkov', '4'")
print(dbcon.select('News', 'post_code'))
