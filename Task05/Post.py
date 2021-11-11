from datetime import datetime


class Post:
    def __init__(self, text, name):
        self.name = name
        self.text = text
        self.post_date = datetime.today()
        self.date_formatted = self.post_date.strftime('%d/%m/%Y %H.%M')

    def printName(self):
        print(self.name)

    def printText(self):
        print(self.text)

