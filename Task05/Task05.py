class MyExample:
    def __init__(self, who, legs):
        self.legs = legs
        self.who = who

    def printIt(self):
        print(f'{self.who} has {self.legs} legs')


qqq = MyExample('spider', 6)

qqq.printIt()