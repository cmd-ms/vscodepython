#__init__

class tweet:
    def __init__(self,message):
        self.y = message


x = tweet("hello people")
print(x.y)

class tweet1:
    def __init__(self,message):
        self.message = message
    def print_tweet1(self):
        print(self.message)

a = tweet1(1)
b = tweet1(2)

a.print_tweet1()
b.print_tweet1()

tweet1.print_tweet1(a)
tweet1.print_tweet1(b)