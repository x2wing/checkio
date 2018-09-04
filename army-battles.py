# Taken from mission The Warriors


class Warrior:
    def __init__(self):
        self.health = 50
        self.is_alive = True
        self.attack = 5

    def make_demage(self, contestant) -> None:
        contestant.take_demage(self.attack)

    def take_demage(self, attack_hit):
        self.health -= attack_hit
        if self.health <= 0:
            self.is_alive = False

    # def get_health(self):
    #     return self.health


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack += 2


def fight(unit_1, unit_2) -> bool:
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.make_demage(unit_2)
        if not unit_2.is_alive: return True
        unit_2.make_demage(unit_1)
        if not unit_1.is_alive: return False


class Army:
    def __init__(self):
        self.army_health = 0
        self.army_attack = 0

    def add_units(self, solder: Warrior, amt):
        solder = solder()
        self.army_health += amt * solder.health
        self.army_attack += amt * solder.attack
        print(self.army_health, self.army_attack)


class Battle:
    def __init__(self):
        self.win = None

    # def fight(self, army1: Army, army2: Army) -> bool:
    #     army1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    # battle = Battle()
    #
    # assert battle.fight(my_army, enemy_army) == True
    # assert battle.fight(army_3, army_4) == False
    # print("Coding complete? Let's try tests!")
