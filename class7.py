

class Thing3():
    def __init__(self):
        self.letters = 'zyx'
x = Thing3()
print(x.letters)


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
test_obiect = Element('Hydrogen', 'H', 1)

    def dump(self):
        print_dump = (self.name,)

