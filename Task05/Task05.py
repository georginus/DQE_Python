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


