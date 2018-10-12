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

    def __init__(self, hp):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)
        # self.hp = hp


class Boss(Monster):
    'boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
print(a3.whoami())

# user1 = Player('tom', 100, 'warr')
# user2 = Player('jerry', 80, 'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()
