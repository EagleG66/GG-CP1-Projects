# GLENN GUDMUNSON combat game

import random


monster = [30, 15, 4, 4]

def playerTurn():

    attack_type = input("""What action would you like to take?
    1. Normal attack
    2. Special attack(You may hurt yourself but you will do more damage!)
    3. Drink a health potion(regain 9 health)
    """)

    if attack_type == 1:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster.replace(monster[0], monster[0] - (random.randint(1, 8)+player[3]))
            print("You hit!")
            print(f"The monster has {monster[0]} health left!")
        else:
            print("You missed!")
    elif attack_type == 2:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster.replace(monster[0], monster[0] - (random.randint(1, 8)+player[3]))
            print("You hit!")
            print(f"The monster has {monster[0]} health left!")
        else:
            print("You missed!")
        player.replace(player[0], player[0] - player[4])
    elif attack_type == 3:
        player.replace(player[0], player[0] + 9)

def monsterTurn():

    attack_type = random.randint(1, 3)

    if attack_type == 1:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster.replace(monster[0], monster[0] - (random.randint(1, 8)+player[3]))
            print("You hit!")
            print(f"The monster has {monster[0]} health left!")
        else:
            print("You missed!")
    elif attack_type == 2:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster.replace(monster[0], monster[0] - (random.randint(1, 8)+player[3]))
            print("You hit!")
            print(f"The monster has {monster[0]} health left!")
        else:
            print("You missed!")
        player.replace(player[0], player[0] - player[4])
    elif attack_type == 3:
        player.replace(player[0], player[0] + 9)


#REPLACE EVERY "PLAYER" WITH "MONSTER" AND VICE VERSA IN THE MONSTER TURN FUNCTION



    


while True:

    print("Welcome to training! First I need to know some things about you!\n")

    user_name = input("What is your name: ")

    fighter_type = input("""
    what type of fighter are you?
    - soldier[1]
    - rogue[2]
    - mage[3]
    """)

    print("An orc is attacking you!\n")

    if fighter_type == 1:
        player = [30, 15, 3, 5, 1]
    elif fighter_type == 2:
        player = [30, 12, 6, 3, 2]
    elif fighter_type == 3:
        player = [30, 11, 4, 6, 4]
    





