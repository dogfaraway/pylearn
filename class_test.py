class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):
        print('%s: %s' % (self.name, self.hp))


user1 = Player('tom', 100)
user2 = Player('jerry', 80)
user1.print_role()
user2.print_role()
