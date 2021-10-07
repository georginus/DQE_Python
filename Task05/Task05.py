class MyExample:
    def __init__(self, who, legs):
        self.legs = legs
        self.who = who

    def printIt(self):
        print(f'{self.who} has {self.legs} legs')


spider = MyExample('Spider', 6)
human = MyExample('Human', 2)

spider.printIt()
human.printIt()


class Post:
    def __init__(self, name):
        self.name = name


class Adv(Post):
    def customer(self):
        print('customer is Epam')

    pass


post = Post('News')
adv = Adv('Adv')

print(post.name)
print(adv.name, ' ', adv.customer())
