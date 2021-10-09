from datetime import datetime, date


class Post:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.post_date = datetime.today()

    def printName(self):
        print(self.name)

    def printText(self):
        print(self.text)


class PrivateAd(Post):
    def __init__(self, name, text, end_date):
        Post.__init__(self, name, text)
        self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        self.delta = (self.end_date - self.post_date.date()).days

    def printAdv(self):
        print(f'{self.name} ------------------\n{self.text}\nActual until: {self.end_date}, {self.delta} days left\n------------------------------')


class News(Post):
    def __init__(self, name, text, end_date):
        Post.__init__(self, name, text)
        self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        self.delta = (self.end_date - self.post_date.date()).days

    def printAdv(self):
        print(f'{self.name} ------------------\n{self.text}\nActual until: {self.end_date}, {self.delta} days left\n------------------------------')


post = Post('News', datetime.today())

qqq = PrivateAd('Private Ad', 'TEXT', '31/10/2021')
qqq.printAdv()
