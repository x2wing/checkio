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
