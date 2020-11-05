class OddEvenSeparator:
    def __init__(self):
        self.ch = []
        self.ne = []

    def add_number(self, a):
        if a % 2 == 0:
            self.ch.append(a)
        else:
            self.ne.append(a)

    def even(self):
        return self.ch

    def odd(self):
        return self.ne
