class Button:
    def __init__(self):
        count = 0

    def click(self):
        self.count += 1

    def click_count(self):
        return(self.count)

    def resert(self):
        self.count = 0
