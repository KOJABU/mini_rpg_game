class Character:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = value
    
import random

class Character:
    def __init__(self, name, health, attack):
        self._name = name
        self._health = health
        self._attack = attack

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @property
    def attack(self):
        return self._attack

    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        self.health -= damage


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=15)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=20)


class Thief(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack=25)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack=18)


class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack=10)

    def heal(self, target):
        target.health += 20


class Monster(Character):
    def __init__(self, name, health, attack, description):
        super().__init__(name, health, attack)
        self.description = description


def choose_enemy():
    monsters = [
        Monster("Goblin", health=50, attack=10, description="A small and vicious creature."),
        Monster("Orc", health=80, attack=15, description="A powerful and brutal warrior."),
        Monster("Dragon", health=150, attack=25, description="A fearsome and fire-breathing dragon."),
        # Добавьте еще монстров по аналогии
    ]
    return random.choice(monsters)


def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name} health: {player.health}, {enemy.name} health: {enemy.health}")
        player_choice = input("Do you want to attack or heal? (a/h): ")
        if player_choice == "a":
            enemy.take_damage(player.attack)
            player.take_damage(enemy.attack)
            print(f"You hit {enemy.name} for {player.attack} damage!")
        elif player_choice == "h" and isinstance(player, Cleric):
            player.heal(player)
            print(f"{player.name} healed themselves!")
        enemy.take_damage(player.attack)
        print(f"{enemy.name} attacks {player.name} for {enemy.attack} damage!")
    if player.is_alive():
        print("You defeated the enemy!")
    else:
        print("You were defeated.")


if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    player_class = input("Choose a class (Warrior, Mage, Thief, Archer, Cleric): ").lower()

    if player_class == "warrior":
        player = Warrior(player_name)
    elif player_class == "mage":
        player = Mage(player_name)
    elif player_class == "thief":
        player = Thief(player_name)
    elif player_class == "archer":
        player = Archer(player_name)
    elif player_class == "cleric":
        player = Cleric(player_name)
    else:
        print("Invalid class choice. Defaulting to Warrior.")
        player = Warrior(player_name)

    while True:
        enemy = choose_enemy()
        print(f"A wild {enemy.name} appears!\n{enemy.description}")
        input("Press Enter to start the battle.")
        battle(player, enemy)

        if not player.is_alive():
            print("Game Over.")
            break
        else:
            print("You defeated the enemy! Ready for the next battle?\n")
            continue
