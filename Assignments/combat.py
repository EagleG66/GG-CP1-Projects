# GLENN GUDMUNSON combat game

import random


monster = [30, 14, 4, 4, 3]




#PLAYER FUNCTION

def playerTurn():

    
    while True:
        try:
            attack_type = int(input("""What action would you like to take?
        
            1. Normal attack
            2. Special attack(You will hurt yourself but you will do more damage!)
            3. Drink a health potion(regain 9 health)
            \n\n"""))
            print("\033[H\033[J", end="")
        except:
            print("That is not a number. Please Try Again.")
        else:
            if attack_type >= 1 and attack_type <= 3:
                break
            else:
                print("That is not one of the options. Please Try Again.")


    # Normal Attack
    if attack_type == 1:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster[0] = monster[0] - (random.randint(1, 8)+player[3])
            print("You hit!\n\n")
        else:
            print("You missed!\n\n")

    # Special Attack
    elif attack_type == 2:
        chance = random.randint(1, 20)
        if chance+player[2] > monster[1]:
            monster[0] = monster[0] - (random.randint(1, 8)+player[3])
            print("You hit!\n\n")
        else:
            print("You missed!\n\n")
        player[0] = player[0] - player[4]

    # Health potion
    elif attack_type == 3:
        if player[0] >= 21:
            player[0] = player[0] + (30 - player[0])
        else:
            player[0] = player[0] + 9



    if player[0] <= 0 and monster[0] <= 0:
        player[0] = 0
        monster[0] = 0
    elif player[0] <= 0:
        player[0] = 0
    elif monster[0] <= 0:
        monster[0] = 0

    print(f"""Here are your stats:

    Health: {player[0]}
    Defense: {player[1]}
    Attack: D20 + {player[2]}
    Damage: D8 + {player[3]}""")


    print(f"""Here are the monster's stats:
    Health: {monster[0]}
    Defense: {monster[1]}
    Attack: D20 + {monster[2]}
    Damage: D8 + {monster[3]}\n\n""")

    if monster[0] > 0 and player[0] > 0:
        return True
    else:
        return False








#MONSTER FUNCTION

def monsterTurn():

    attack_type = random.randint(1, 3)


    # Normal Attack
    if attack_type == 1:
        chance = random.randint(1, 20)
        if chance+monster[2] > player[1]:
            player[0] = player[0] - (random.randint(1, 8)+monster[3])
            print("They hit!\n\n")
        else:
            print("They missed!\n\n")

    # Special Attack
    elif attack_type == 2:
        chance = random.randint(1, 20)
        if chance+monster[2] > player[1]:
            player[0] = player[0] - (random.randint(1, 8)+monster[3])
            print("They hit you with a special attack!\n\n")
        else:
            print("They missed!\n\n")
        monster[0] = monster[0] - monster[4]

    # Health Potion
    elif attack_type == 3:
        if monster[0] >= 22:
            monster[0] = monster[0] + (30 - monster[0])
        else:
            monster[0] = monster[0] + 8

        print("They drank a health potion to regain health!\n\n")

    if player[0] <= 0 and monster[0] <= 0:
        player[0] = 0
        monster[0] = 0
    elif player[0] <= 0:
        player[0] = 0
    elif monster[0] <= 0:
        monster[0] = 0

    print(f"""\n\nHere are your stats:
    Health: {player[0]}
    Defense: {player[1]}
    Attack: D20 + {player[2]}
    Damage: D8 + {player[3]}""")

    print(f"""Here are the monster's stats:
    Health: {monster[0]}
    Defense: {monster[1]}
    Attack: D20 + {monster[2]}
    Damage: D8 + {monster[3]}\n\n""")

    if monster[0] > 0 and player[0] > 0:
        return True
    else:
        return False



    
print("\033[H\033[J", end="")

while True:

    print("Welcome to training! First I need to know some things about you!\n")


    while True:
        try:
            user_name = input("What is your name: ")
            print("\033[H\033[J", end="")

    while True:
        try:
            fighter_type = int(input("""\n\n
            what type of fighter are you?
            - soldier[1]
            - rogue[2]
            - mage[3]
            \n\n"""))
            print("\033[H\033[J", end="")
        except:
            print("That is not a number. Please Try Again.")
        else:
            if fighter_type >= 1 and fighter_type <= 3:
                break
            else:
                print("That is not one of the options. Please Try Again.")
            


    if fighter_type == 1:
        player = [30, 15, 3, 5, 1]
    elif fighter_type == 2:
        player = [30, 12, 6, 3, 2]
    elif fighter_type == 3:
        player = [30, 11, 4, 6, 4]


    print(f"""\n\nHere are your stats:
    Health: {player[0]}
    Defense: {player[1]}
    Attack: D20 + {player[2]}
    Damage: D8 + {player[3]}\n\n""")


    print("An orc is attacking you!\n\n")


    print(f"""Here are the monster's stats:
    Health: {monster[0]}
    Defense: {monster[1]}
    Attack: D20 + {monster[2]}
    Damage: D8 + {monster[3]}\n\n""")

    while monsterTurn() and playerTurn():
        continue

    if player[0] <= 0 and monster[0] <= 0:
        print("You both died! GAME OVER")
    elif player[0] <= 0:
        print("The orc killed you. GAME OVER")
    elif monster[0] <= 0:
        print("You won the battle! Congrats!")


    if input("Would you like to play again?(Type anything and press ENTER for yes, Just press ENTER for no): "):
        continue
    else:
        break


    





