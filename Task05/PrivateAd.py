from Post import Post
from datetime import datetime, date


class PrivateAd(Post):
    def __init__(self, text, end_date, name='PrivateAd'):
        Post.__init__(self, text, name)
        self.end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        self.delta = (self.end_date - self.post_date.date()).days
        self.end_date_formatted = self.end_date.strftime('%d/%m/%Y')
        self.post = ''

    def printPost(self):
        return (
            f'{self.name} -------------------\n{self.text}\nActual until: {self.end_date_formatted}, {self.delta} days '
            f'left\n------------------------------\n\n')
