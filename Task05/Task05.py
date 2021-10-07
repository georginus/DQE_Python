class MyExample:
    def __init__(self, who, legs):
        self.legs = legs
        self.who = who

    def printIt(self):
        print(f'{self.who} has {self.legs} legs')


spider = MyExample('Spider', 6)
human = MyExample('Human', 2)

#spider.printIt()
#human.printIt()


class Post:
    def __init__(self, name):
        self.name = name


class Adv(Post):
    def __init__(self, name, customer):
        Post.__init__(self, name)
        self.customer = customer

    def customer_is(self):
        print(f'{self.name}: customer is {self.customer}')



post = Post('News')
adv = Adv('Adv', 'Epam')
adv.customer_is()


