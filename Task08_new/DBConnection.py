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
        print(f"Inserted into {table}")
        self.connection.commit()

    def checkNewsDuplicates(self, post_code, post_text, post_city):
        return self.cur.execute(f'select count(*) from News as N where N.post_code = {post_code} '
                                f'and N.post_text = \'{post_text}\' '
                                f'and N.post_city = \'{post_city}\'').fetchall()[0][0]

    def checkPrivateAdDuplicates(self, post_code, post_text, expiration_date):
        return self.cur.execute(f'select count(*) from PrivateAd where post_code = {post_code} '
                                f'and post_text = \'{post_text}\''
                                f'and expiration_date = \'{expiration_date}\'').fetchall()[0][0]

    def checkLifehackDuplicates(self, post_code, post_text, hashtag):
        return self.cur.execute(f'select count(*) from Lifehack where post_code = {post_code} '
                                f'and post_text = \'{post_text}\' '
                                f'and hashtag = \'{hashtag}\'').fetchall()[0][0]

    def insertNews(self, post_code, post_text, post_city, post_date):
        # print(self.checkNewsDuplicates(post_code, post_text, post_city))
        if self.checkNewsDuplicates(post_code, post_text, post_city) >= 1:
            print(f'Record {post_code}, {post_text}, {post_city} already exists')
        else:
            self.cur.execute(f"insert into News values ({post_code}, 'News', \'{post_text}\', \'{post_city}\', \'{post_date}\')")
            print(f"Inserted into News")
            self.connection.commit()

    def insertPrivateAd(self, post_code, post_text, post_date):
        if self.checkPrivateAdDuplicates(post_code, post_text, post_date) >= 1:
            print(f'Record {post_code}, {post_text}, {post_date} already exists')
        else:
            self.cur.execute(f"insert into PrivateAd values ({post_code}, 'PrivateAd', \'{post_text}\', \'{post_date}\')")
            print(f"Inserted into PrivateAd")
            self.connection.commit()

    def insertLifehack(self, post_code, post_text, hashtag, post_date):
        if self.checkLifehackDuplicates(post_code, post_text, hashtag) >= 1:
            print(f'Record {post_code}, {post_text}, {hashtag} already exists')
        else:
            self.cur.execute(
                f"insert into Lifehack values ({post_code}, 'Lifehack', \'{post_text}\', \'{hashtag}\', \'{post_date}\')")
            print(f"Inserted into Lifehack")
            self.connection.commit()

    def closeCursor(self):
        self.cur.close()

