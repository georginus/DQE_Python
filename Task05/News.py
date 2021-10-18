from Post import Post


class News(Post):
    def __init__(self, text, city, name='News'):
        Post.__init__(self, text, name)
        self.city = city

    def printPost(self):
        return (f'{self.name} -------------------------\n{self.text}\n{self.city}, {self.date_formatted}\n'
                f'------------------------------\n\n')
