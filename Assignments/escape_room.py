# GLENN GUDMUNSON escape room
import time

code = 7700
hint_num = 1
fail = True
time_left = 600

print("You have been locked in the janitor's closet by the class bully!!! There is a padlock that you must find the four-digit code for to escape. However, your classmate is diabolical and he is pumping poison gas into the room. Each action you take \nwill use up 30 seconds of the precious 10 minutes you have. Good luck!")
input("\n\n\nPress ENTER when you are done reading.")
print("\033[H\033[J", end="")

for i in range(14):

    while True:
        try:
            action = int(input("Type in the corresponding number for the action you would like to take(1.type in code 2.look a direction 3.exit the program): "))
            print("\033[H\033[J", end="")
        except:
            print("That is not a number!")
            time.sleep(3)
            print("\033[H\033[J", end="")
        else:
            if action > 3 or action < 1:
                print("That is not one of the options!")
                time.sleep(3)
                print("\033[H\033[J", end="")
            else:
                break


    if action == 3:
        fail = False
        break
        

    elif action == 1:
        while True:
            try:
                code_input = int(input("What is the code?(four digits): "))
            except:
                print("That is not a number!!!")
                input("\n\n\nPress ENTER when you are done reading.")
                print("\033[H\033[J", end="")
            else:
                fail = False
                break
        print("\033[H\033[J", end="")

        if code_input == code:
            print("Congrats! You have escaped the closet! You may now go lock your \"friend\" in the closet and they will have to escape. Just pump the poison faster and maybe he won't make it...")
            break
        else:
            print("You failed to input the correct code. Here is a hint to help you out:\n\n\n")

            if hint_num == 1:
                print("Numbers are the key")
                input("\n\n\nPress ENTER when you are done reading.")
                print("\033[H\033[J", end="")
            elif hint_num == 2:
                print("Look closely, because it is a pretty design")
                input("\n\n\nPress ENTER when you are done reading.")
                print("\033[H\033[J", end="")
            elif hint_num == 3:
                print("\"WHAT IS THE DIFFERENCE?\"")
                input("\n\n\nPress ENTER when you are done reading.")
                print("\033[H\033[J", end="")
                hint_num -= 3
            hint_num += 1
    elif action == 2:

        while True:
            try:
                direction = input("Which direction would you like to look?(right, left, up, down, backward, forward): ").lower()
                print("\033[H\033[J", end="")
            except:
                print("That is not an option!!!")
                input("\n\n\nPress ENTER when you are done reading.")
                print("\033[H\033[J", end="")
            else:
                if direction != "right" and direction != "left" and direction != "up" and direction != "down" and direction != "backward" and direction != "forward":
                    print("That is not one of the specified options!")
                    input("\n\n\nPress ENTER when you are done reading.")
                    print("\033[H\033[J", end="")
                else:
                    break

        if direction == "right":
            print("""You look to your right and discover a note that says the following: 
                  
                  Dear, Sylvia
                  
                  \tI have been thinking about you lately, and I want you to know that I miss you. You always knew how to make me smile, and I
                  \tloved the beautiful dress you wore every thursday. I was hoping we could meet up when you're free. I can reserve a beautiful
                  \trestaurant in the mountains with an extraordinary view. The address is 9741 W 9700 N Orem UT. Please tell me if you can come
                  \tsometime. I would love to see you and catch up with you. 
                  
                  \t\t\t\t\t\t\t\t\t\t\t\t\t\tSincerely, Jim
                  
                  You decide that the next best course of action is to take the note off the wall to find anything else that could help. However,
                  all you find is some black marks on the wall, likely from somebody hitting it with something.""")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

        if direction == "left":
            print(""""You turn to your left and discover a map that views the entire city of Orem. You also notice that there is a spot on the
                  map that is circled. The address of that spot is 120 N 2000 E. You decide to take the map down to see if anything is behind it,
                  and you find an riddle etched into the wall: Find one place and you will fail. Find two places and you will be close. What is the 
                  difference?""")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

        if direction == "up":
            print("You lift your eyes up to a vent in the ceiling. However, it is very high up. You would need something to climb up to get out.")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

        if direction == "down":
            print("""You notice you are standing on a carpet with an interesting design:
                  
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=2===+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++==n==+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----++d++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++===n=+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++---u-+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+m+++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++===b=+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++==e==+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+r+++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----
                  -----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----+++++=====+++++-----""")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

        if direction == "backward":
            print("""You turn around and find a desk with an open computer on it. Unfortunately, it is locked and you do not know the code. You also 
                  notice a note stuck to the table next to the device. It has a list of names on it:
                  
                  Allan
                  Tyler
                  Sammy
                  Bruno
                  Mykel
                  Tommy
                  Randy
                  
                  You find your name on it, as well as the kid that locked you in here.""")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

        if direction == "forward":
            print("In front of you lies the door to get out with a 4-digit code. You attempt to break the lock with a hard punch, but only hurt yourself.")
            input("\n\n\nPress ENTER when you are done analyzing.")
            print("\033[H\033[J", end="")

    time_left -= 30
    print(f"You have {time_left} seconds left!!!")    

       
if fail:
    print("The poison gas killed you before you could enter the correct code. You may try again if you would like.")
else:
    pass

            