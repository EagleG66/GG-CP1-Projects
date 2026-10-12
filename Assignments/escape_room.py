# GLENN GUDMUNSON escape room

code = 1234
hint_num = 1
fail = True
time = 300

print("You have been locked in the janitor's closet by the class bully!!! There is a padlock that you must find the four-digit code for to escape. However, your classmate is diabolical and he is pumping poison gas into the room. Each action you take \nwill use up 30 seconds of the precious 5 minutes you have. Good luck!")

for i in range(10):

    while True:
        try:
            action = int(input("Type in the corresponding number for the action you would like to take(1.type in code 2.look a direction 3.exit the program): "))
        except:
            print("That is not a number!")
        else:
            if action > 3 or action < 1:
                print("That is not one of the options!")
            else:
                break


    if action == 3:
        fail = False
        break
        

    elif action == 1:
        code_input = input("What is the code?(four digits): ")

        if code_input == code:
            print("Congrats! You have escaped the closet! You may now go lock your \"friend\" in the closet and they will have to escape. Just pump the poison faster and maybe he won't make it.")
        else:
            print("You failed to input the correct code. Here is a hint to help you out!")

            if hint_num == 1:
                print("hint1")
            elif hint_num == 2:
                print("hint2")
            elif hint_num == 3:
                print("hint3")
            elif hint_num == 4:
                print("hint4")
            elif hint_num == 5:
                print("hint5")
                hint_num -= 5
            hint_num += 1
    elif action == 2:

        while True:
            try:
                direction = input("Which direction would you like to look?(right, left, up, down, backward, forward): ").lower()
            except:
                print("That is not an option!!!")
            else:
                if direction != "right" and direction != "left" and direction != "up" and direction != "down" and direction != "backward" and direction != "forward":
                    print("That is not one of the specified options!")
                else:
                    break

        if direction == "right":
            print("""You look to your right and discover a note that says the following: 
                  
                  Dear, Sylvia
                  
                  \tI have been thinking about you lately, and I want you to know that I miss you. You always knew how to make me smile, and I
                  \tloved the beautiful dress you wore every thursday. I was hoping we could meet up or something""")

        if direction == "left":
            print("left")

        if direction == "up":
            print("up")

        if direction == "down":
            print("down")

        if direction == "backward":
            print("backward")

        if direction == "forward":
            print("forward")

    time -= 30
    print(f"You have {time} seconds left!!!")    

        
if fail:
    print("The poison gas killed you before you could enter the correct code. You may try again if you would like.")
else:
    pass

            