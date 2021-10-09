from datetime import datetime, date


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


class PrivateAd(Post):
    def __init__(self, text, end_date, name='PrivateAd'):
        Post.__init__(self, text, name)
        self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        self.delta = (self.end_date - self.post_date.date()).days
        self.end_date_formatted = self.end_date.strftime('%d/%m/%Y')
        self.post = ''

    def printPost(self):
        self.post = (
            f'{self.name} -------------------\n{self.text}\nActual until: {self.end_date_formatted}, {self.delta} days '
            f'left\n------------------------------\n\n')


class News(Post):
    def __init__(self, text, city, name='News'):
        Post.__init__(self, text, name)
        self.city = city

    def printPost(self):
        return (f'\n{self.name} -------------------------\n{self.text}\n{self.city}, {self.date_formatted}\n'
                f'------------------------------\n')


class LifeHack(Post):
    def __init__(self, text, hashtag, name='LifeHack'):
        Post.__init__(self, text, name)
        self.hashtag = hashtag
        self.post = ''

    def printPost(self):
        self.post = (f'{self.name} -------------------------\n{self.text}\n#{self.hashtag}, {self.date_formatted}\n'
                     f'------------------------------\n\n')


# class OutputFile:
#     def __init__(self, post, file_path='~/', file_name='output.txt'):
#         self.path = file_path
#         self.file_name = file_name
#         self.post = post
#
#     def openFile(self):
#         f = open(self.file_path + self.file_name, 'a')
#
#     def writeIntoFile(self):
#         f.write(self.post)
#
#     def closeFile(self):


def formPost():
    is_input_correct = False
    while not is_input_correct:
        post_code = int(input(f'Input Post code:\n\t1 - News\n\t2 - Private Ad\n\t3 - LifeHack\n'))
        if 0 < post_code < 4:
            break
        else:
            print(f'Incorrect Post code. Please try again...\n')
    if post_code == 1:
        text = input('Enter News text:')
        city = input('Enter News city:')
        news = News(text, city)
        post = news.printPost()
    elif post_code == 2:
        text = input('Enter Private Ad text:')
        end_date = input('Enter Private Ad end date(dd/mm/yyyy):')
        PrivateAd(text, end_date).printPost()
    else:
        text = input('Enter LifeHack text:')
        hashtag = input('Enter LifeHack hashtag:')
        LifeHack(text, hashtag).printPost()
    return post


# ---Main---
file_path = ''
file_name = 'output.txt'
f = open(file_path + file_name, 'a+')
if_continue = 'y'
while if_continue == 'y':
    f.write(formPost())
    if_continue = input('Do you want to continue?(y/N)')
f.close()
