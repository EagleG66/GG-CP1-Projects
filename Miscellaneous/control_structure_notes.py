# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   BOOLEANS
import random

win = False
my_num = random.randint(0,20)

while win == False:
    num = int(input("Pick a number between 0 and 20: "))
    if num == my_num:    #<<<BOOLEAN EQUATION
        win = True
        print("YOU WIN!!!")
    elif num < my_num:
        print("HIGHER!!!")
    elif num > my_num:
        print("LOWER!!!")

# Note: if empty quotations or 0, FALSE, else TRUE
print(bool(my_num))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   CONDITIONALS