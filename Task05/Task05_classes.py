from datetime import datetime, date


class Post:
    def __init__(self, name):
        self.name = name
        self.text = ''
        self.post_date = datetime.today()
        self.date_formatted = self.post_date.strftime('%d/%m/%Y %H.%M')

    def setText(self):
        self.text = input('Enter text:')

    def printName(self):
        print(self.name)

    def printText(self):
        print(self.text)


class PrivateAd(Post):
    def __init__(self, name='Private Ad', end_date=datetime.today().date()):
        Post.__init__(self, name)
        self.end_date = end_date
        self.delta = 0
        self.end_date_formatted = end_date

    def set_end_date(self):
        self.end_date = datetime.strptime(input('Enter end date(dd/mm/yyyy):'), '%d/%m/%Y').date()
        self.end_date_formatted = self.end_date.strftime('%d/%m/%Y')
        self.delta = (self.end_date - self.post_date.date()).days

    def printPost(self):
        print(
            f'{self.name} -------------------\n{self.text}\nActual until: {self.end_date_formatted}, {self.delta} days '
            f'left\n------------------------------\n')


class News(Post):
    def __init__(self, city='Minsk', name='News'):
        Post.__init__(self, name)
        self.city = city

    def set_city(self):
        self.city = input('Enter city:')

    def printPost(self):
        print(f'{self.name} -------------------------\n{self.text}\n{self.city}, {self.date_formatted}\n'
              f'------------------------------\n')


class LifeHack(Post):
    def __init__(self, hashtag, name='LifeHack'):
        Post.__init__(self, name)
        self.hashtag = hashtag

    def printPost(self):
        print(f'{self.name} -------------------------\n{self.text}\n#{self.hashtag}, {self.date_formatted}\n'
              f'------------------------------\n')


ad1 = PrivateAd()
ad1.setText()
ad1.set_end_date()
ad1.printPost()

news1 = News('Minsk')
news1.setText()
news1.printPost()

lifehack1 = LifeHack('Food')
lifehack1.setText()
lifehack1.printPost()


def formPost():
    is_input_correct = False
    while not is_input_correct:
        post_code = int(input(f'Input Post code:\n\t1 - News\n\t2 - Private Ad\n\t3 - LifeHack3\n'))
        if 0 < post_code < 4:
            break
        else:
            print(f'Incorrect Post code. Please try again...\n')
    if post_code == 1:
        pass
        #buildNews('News')
    elif post_code == 2:
        pass
        #buldPrivateAd()
    else:
        pass
        #buildLifeHack()


#formPost()
