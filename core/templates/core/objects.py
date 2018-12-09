class Say:

    def __init__(self, first, last):
        self.nn = first
        self.nnn=last
        self.email=first+'.'+ last+'@dexter.com'

    def sum(self):
        return '{} {}'.format(self.nn, self.nnn)

var= Say('alex', 'torres')

var.sum()
print(var.sum())
print(Say.sum(var))