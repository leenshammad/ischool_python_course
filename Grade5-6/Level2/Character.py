class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def attack(self):
        print(f"{self.name} performs a basic attack.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name, health, level, strength):
        super().__init__(name, health, level)
        self.strength = strength

    def attack(self):
        damage = self.strength * 2
        print(f"{self.name} swings a sword for {damage} damage!")

    def shield_block(self):
        print(f"{self.name} blocks the next attack with a shield.")


class Mage(Character):
    def __init__(self, name, health, level, mana):
        super().__init__(name, health, level)
        self.mana = mana

    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts a fireball!")
        else:
            print(f"{self.name} does not have enough mana.")

    def teleport(self):
        print(f"{self.name} teleports to a safe location.")


class Archer(Character):
    def __init__(self, name, health, level, agility):
        super().__init__(name, health, level)
        self.agility = agility

    def attack(self):
        damage = self.agility * 1.5
        print(f"{self.name} shoots an arrow for {damage} damage!")

    def multi_shot(self):
        print(f"{self.name} fires multiple arrows at once.")


warrior = Warrior("Thor", 120, 5, 15)
mage = Mage("Merlin", 80, 7, 50)
archer = Archer("Robin", 90, 6, 12)

warrior.attack()
mage.attack()
archer.multi_shot()