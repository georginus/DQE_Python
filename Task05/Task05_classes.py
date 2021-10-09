class Post:
    def __init__(self, name):
        self.name = name

    def publish_date(self):
        print('Today')


class Adv(Post):
    def __init__(self, name, customer):
        Post.__init__(self, name)
        self.customer = customer

    def customer_is(self):
        print(f'{self.name}: customer is {self.customer}')