class door:
    def __init__(self, num):
        self.num = num
        self.behind = []
        self.selected = False
        self.other = False
    def assign_door(self, prize):
        self.behind.append(prize)
    def select_door(self, chosen):
        if chosen == True:
            self.selected = True
    def other_door(self, other):
        if other == True:
            self.other = True