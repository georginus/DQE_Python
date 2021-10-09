from Post import Post


class LifeHack(Post):
    def __init__(self, text, hashtag, name='LifeHack'):
        Post.__init__(self, text, name)
        self.hashtag = hashtag
        self.post = ''

    def printPost(self):
        return (f'{self.name} -------------------------\n{self.text}\n#{self.hashtag}, {self.date_formatted}\n'
                     f'------------------------------\n\n')