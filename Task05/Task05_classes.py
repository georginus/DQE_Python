import re
from datetime import datetime
from sqlite3 import Date


class Post:
    def __init__(self, name):
        self.name = name

    def publish_date(self):
        print(Date.today())


class Adv(Post):
    def __init__(self, name, customer):
        Post.__init__(self, name)
        self.customer = customer

    def customer_is(self):
        print(f'{self.name}: customer is {self.customer}')

post = Post('News')