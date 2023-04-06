import random

# defining dice object
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, print_result= True):
        rolled = random.randint(1, self.sides)
        result = f"The dice rolled {rolled}"
        if print_result:
            print(result)
        return rolled

# creating dices
d20 = Dice(20)
d100 =Dice(100)

# defining weapon object with attributes
class Weapon:
    def __init__(self, name, damage: float or int, is_ranged: bool):
        self.name = name
        self.damage = damage
        self.is_ranged = is_ranged

# creating weapons
knife = Weapon('Knife', 90, False)
colt_pistol = Weapon('Colt 1851', 250, True)

# defining Player object with attributes
class Player:
    def __init__(self, name, health, base_damage, weapon):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.d20 = d20
        self.weapon: Weapon = weapon

    # checks if player is alive
    @property
    def is_alive(self):
        return self.health > 0

    # calculate the damage
    # if the weapon is ranged the damage is only the weapon damage
    # if the weapon is not ranged the damage is calculated with the player base_damage and weapon damage
    @property
    def damage(self):
        final_damage = self.weapon.damage + self.base_damage
        if self.weapon.is_ranged:
            return self.weapon.damage * (d20.roll() / 10)
        return final_damage * (d20.roll() / 10)

    # attack function that returns the status of players
    def attack(self, enemy):
        print(self.name, 'attacks', enemy.name, "")
        applied_damage = self.damage
        enemy.health -= applied_damage
        print(
            f"{enemy.name} received the attack ({int(applied_damage)}) and it's health is now ({int(enemy.health)}/{enemy.max_health})")
        print('>')

    # roll d100 for initiative
    def iniciative(self):
        return d100.roll(False)

    @property
    def status(self):
        return "wins!" if self.is_alive else "was defeated"

# creating players
tarantino = Player("Tarantino", 800, 30, colt_pistol)
scarlet = Player("Scarlet", 800, 40, knife)


def combat(player1, player2):
    print(f'Fight!\n{player1.name} X {player2.name}')
    print(f'> {player1.name} is using {player1.weapon.name}\n> {player2.name} is using {player2.weapon.name}')
    print('-' * 30)

    # Determine initiative order
    initiative1 = player1.iniciative()
    initiative2 = player2.iniciative()

    # Handling the same initiative
    while initiative1 == initiative2:
        print("It's a tie! Rolling the dice again...")
        initiative1 = player1.iniciative()
        initiative2 = player2.iniciative()

    print(f"{player1.name} rolls {initiative1} for initiative.")
    print(f"{player2.name} rolls {initiative2} for initiative.")

    if initiative1 > initiative2:
        attacker = player1
        defender = player2
    else:
        attacker = player2
        defender = player1

    print(f"{attacker.name} acts first!")

    # defining rounds
    round = 1
    print('-' * 75, " Round", round)
    while True:
        attacker.attack(defender)
        if not defender.is_alive:
            print(f'{defender.name} has died')
            break

        defender.attack(attacker)
        if not attacker.is_alive:
            print(f'{attacker.name} has died')
            break

        round += 1
        print('-' * 75, " Round", round)

    print(f'End of fight ⚔')
    print(attacker.name, attacker.status)
    print(defender.name, defender.status)

combat(tarantino, scarlet)