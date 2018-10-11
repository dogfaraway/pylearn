class Player():
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print('%s: %s: %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.name = newname

class Monster():
    '定义怪物类'

    pass

user1 = Player('tom', 100, 'warr')
user2 = Player('jerry', 80, 'master')
user1.print_role()
user2.print_role()

user1.updateName('wilson')
user1.print_role()


