# GLENN GUDMUNSON dice roller

import random

while True:
    try:
        dice_type = input("Out of these dice, which one do you want to roll?(D4, D6, D8, D10, D12, D20): ").capitalize()
    except:
        print("That's not right!!!")
    else:
        if dice_type != "D4" and dice_type != "D6" and dice_type != "D8" and dice_type != "D10" and dice_type != "D12" and dice_type != "D20":
            print("THAT'S NOT AN OPTION!!!")
        else:
            break


if dice_type == "D4":
    dice_roll = random.randint(1,4)
elif dice_type == "D6":
    dice_roll = random.randint(1,6)
elif dice_type == "D8":
    dice_roll = random.randint(1,8)
elif dice_type == "D10":
    dice_roll = random.randint(1,10)
elif dice_type == "D12":
    dice_roll = random.randint(1,12)
elif dice_type == "D20":
    dice_roll = random.randint(1,20)

print(f"You rolled a {dice_roll}")