# Combat Logic for RPG

This code is part of an RPG game that simulates a fight between two players, each with a weapon and their own stats. The game is turn-based, and each player takes a turn attacking the other until one of them runs out of health points.

### Dices Logic 🎲 
>Dice logic is an essential part of any **RPG game**, and it is used to add a level of randomness and chance to the game. In this particular code, the Dice class is defined with a constructor that takes the number of sides of the dice as a parameter.
>
>The roll method of the Dice class generates a random integer between 1 and the number of sides of the dice. This simulates rolling the dice in a game. 

**How to interact with the code**

    First, create two player objects with their names, health points, base damage, and weapon.
    Call the combat function with the two player objects as arguments.
    The code will automatically simulate the fight, displaying the results of each attack, the health points of each player, and the winner at the end of the game.

**Objects**

> Dice 

The Dice class represents a dice with a certain number of sides. It has an attribute sides and a roll method that returns a random integer between 1 and the number of sides. It is used to determine initiative and damage.

> Weapon ⚔

The Weapon class represents a weapon with a name, damage points, and a flag that indicates if it is ranged or not. The damage attribute is the total damage that the weapon can cause.

>Player 

The Player class represents a player with a name, health points, base damage, and a weapon. 

    is_alive: returns True if the player's health points are greater than 0, False otherwise.
    damage: calculates the damage points that the player can cause based on their base damage and weapon. If the weapon is ranged, the damage is calculated based on the weapon damage and a random roll of the d20 dice. Otherwise, the damage is calculated based on the sum of the base damage of the player and the weapon damage and a random roll of the d20 dice.
    attack: takes another player object as an argument and simulates an attack by subtracting the damage points from the enemy player's health points.
    iniciative: rolls a Dice object with 100 sides to determine the initiative of the player.
    status: returns "wins!" if the player is alive, "was defeated" otherwise.

**Combat Function**

The combat function takes two player objects as arguments and simulates a fight between them. It determines the initiative order based on the results of each player's initiative roll and alternates attacks until one player's health points reach 0 or below. At the end of the game, it displays the winner and the loser.