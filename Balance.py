class Balance:
    def __init__(self):
        self.l = 0
        self.r = 0

    def add_right(self, k):
        self.r += k

    def add_left(self, k):
        self.l += k

    def result(self):
        if self.r > self.l:
            print("R")
        elif self.l > self.r:
            print("L")
        else:
            print("=")
