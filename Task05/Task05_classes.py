from datetime import datetime, date


class Post:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.post_date = datetime.today()
        self.date_formatted = self.post_date.strftime('%d/%m/%Y %H.%M')

    def printName(self):
        print(self.name)

    def printText(self):
        print(self.text)


class PrivateAd(Post):
    def __init__(self, name, text, end_date):
        Post.__init__(self, name, text)
        self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        self.delta = (self.end_date - self.post_date.date()).days
        self.end_date_formatted = self.end_date.strftime('%d/%m/%Y')

    def printPost(self):
        print(f'{self.name} -------------------\n{self.text}\nActual until: {self.end_date_formatted}, {self.delta} days '
              f'left\n------------------------------\n')


class News(Post):
    def __init__(self, name, text, city):
        Post.__init__(self, name, text)
        self.city = city

    def printPost(self):
        print(f'{self.name} -------------------------\n{self.text}\n{self.city}, {self.date_formatted}\n'
              f'------------------------------\n')


class LifeHack(Post):
    def __init__(self, name, text, hashtag):
        Post.__init__(self, name, text)
        self.hashtag = hashtag

    def printPost(self):
        print(f'{self.name} -------------------------\n{self.text}\n#{self.hashtag}, {self.date_formatted}\n'
              f'------------------------------\n')


ad1 = PrivateAd('Private Ad', 'TEXT', '31/10/2021')
ad1.printPost()

news1 = News('News', 'News text', 'Minsk')
news1.printPost()

lifehack1 = LifeHack('LifeHack', 'Text', 'Food')
lifehack1.printPost()

de