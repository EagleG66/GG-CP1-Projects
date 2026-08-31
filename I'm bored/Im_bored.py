#Glenn Gudmunson FIRST PROJECT
import time
import random
import keyboard as kb
#TIMER
"""
startY = int(input("How many minutes do you want to set the timer for?"))
startX = int(input("How many seconds do you want to set the timer for?"))
x = startX
y = startY
running = True
alarm = False


while running:

    strY = str(y)
    strX = str(x)

    if alarm :
        print("BEEP!")
    else:
        if x >= 10:
            print(strY + ":" + strX)
        else:
            print(strY + ":0" + strX)

    if x <= -1 and alarm == False:
        x = 60
        y -=1

    if y <= 0 and x <= 0:
        alarm = True

    if alarm:
        print("BEEP!")
    else:
        x -= 1
    time.sleep(1)
"""

# MATH 
"""
running = True
seconds = 0
incorrect = False
m1 = random.randint(1,12)
m2 = random.randint(1,12)
a1 = random.randint(1,27)
a2 = random.randint(1,27)
s1 = random.randint(1,27)
s2 = random.randint(1,27)


#math homework
def multiply(num1,num2):
    global answer
    global incorrect
    correct_answer = num1 * num2
    str_num1 = str(num1)
    str_num2 = str(num2)
    answer = int(input("What is " + str_num1 + " x " + str_num2 + " "))
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong! The answer is",correct_answer)
        incorrect = True

def add(num1,num2):
    global answer
    global incorrect
    correct_answer = num1 + num2
    str_num1 = str(num1)
    str_num2 = str(num2)
    answer = int(input("What is " + str_num1 + " + " + str_num2 + " "))
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong! The answer is",correct_answer)
        incorrect = True

def divide(num1,num2):
    global answer
    global incorrect
    correct_answer = num1/num2
    str_num1 = str(num1)
    str_num2 = str(num2)
    answer = int(input("What is " + str_num1 + " / " + str_num2 + " "))
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong! The answer is",correct_answer)
        incorrect = True

def subtract(num1,num2):
    global answer
    global incorrect
    correct_answer = num1 - num2
    str_num1 = str(num1)
    str_num2 = str(num2)
    answer = int(input("What is " + str_num1 + " - " + str_num2 + " "))
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong! The answer is",correct_answer)
        incorrect = True



multiply(m1,m2)
if incorrect == False:
    add(a1,a2)
    if incorrect == False:
        divide(48,6)
        if incorrect == False:
            subtract(s1,s2)
            if incorrect == False:
                print("YIPEEEEE!!!")
            else:
                print("YOU SUCK AT MATH!!!")
        else:
            print("YOU SUCK AT MATH!!!")
    else:
        print("YOU SUCK AT MATH!!!")
else:
    print("YOU SUCK AT MATH!!!")

"""

# FAILED ATTEMPT AT KEYBINDING

print("HELLO WORLD")



# TIC TAC TOE
"""
top_left = " "
top_mid = " "
top_right = " "
mid_right = " "
mid_left = " "
mid_mid = " "
bottom_left = " "
bottom_right = " "
bottom_mid = " "

game_running = True


# GAMEBOARD
print("       |       |       ")
print("   1   |   2   |   3   ")
print("       |       |       ")
print("-------+-------+-------")
print("       |       |       ")
print("   4   |   5   |   6   ")
print("       |       |       ")
print("-------+-------+-------")
print("       |       |       ")
print("   7   |   8   |   9   ")
print("       |       |       ")


# GAMEBOARD
def gameBoard():
    print("       |       |       ")
    print("   "+top_left+"   |   "+top_mid+"   |   "+top_right+"   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   "+mid_left+"   |   "+mid_mid+"   |   "+mid_right+"   ")
    print("       |       |       ")
    print("-------+-------+-------")
    print("       |       |       ")
    print("   "+bottom_left+"   |   "+bottom_mid+"   |   "+bottom_right+"   ")
    print("       |       |       ")


def winCheck(shape):

    global game_running

    if top_left == shape and top_mid == shape and top_right == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif mid_left == shape and mid_mid == shape and mid_right == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif bottom_left == shape and bottom_mid == shape and bottom_right == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif top_left == shape and mid_left == shape and bottom_left == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif top_mid == shape and mid_mid == shape and bottom_mid == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif top_right == shape and mid_right == shape and bottom_right == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif top_left == shape and mid_mid == shape and bottom_right == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False
    elif top_right == shape and mid_mid == shape and bottom_left == shape:
        if shape == "X":
            print("Player 1 Wins!!!")
            game_running = False
        elif shape == "O":
            print("Player 2 Wins!!!")
            game_running = False




while game_running:

    # CHECKING FOR A WIN
    winCheck("O")
    winCheck("X")


    # PLAYER ONE INPUT
    while True:
        try:
            player1_turn = int(input("Player1: Choose a spot based on the correlating number from the diagram above: "))
        except:
            print("THAT'S NOT A NUMBER!!!")
        else:
            if player1_turn < 0 or player1_turn > 9:
                print("THAT'S NOT AN OPTION!!!")
            else:
                break

    
    # PLAYER ONE OUTPUT
    if player1_turn == 1 and top_left == " ":
        top_left = "X"
    elif player1_turn == 2 and top_mid == " ":
        top_mid = "X"
    elif player1_turn == 3 and top_right == " ":
        top_right = "X"
    elif player1_turn == 4 and mid_left == " ":
        mid_left = "X"
    elif player1_turn == 5 and mid_mid == " ":
        mid_mid = "X"
    elif player1_turn == 6 and mid_right == " ":
        mid_right = "X"
    elif player1_turn == 7 and bottom_left == " ":
        bottom_left = "X"
    elif player1_turn == 8 and bottom_mid == " ":
        bottom_mid = "X"
    elif player1_turn == 9 and bottom_right == " ":
        bottom_right = "X"
    else:
        print("YOU FORFEIT YOUR TURN FOR CHOOSING A SPACE THAT WAS TAKEN UP!")

    # PRINT THE BOARD
    gameBoard()


    # CHECKING FOR A WIN
    winCheck("O")
    winCheck("X")

    if game_running:
        # PLAYER TWO INPUT
        while True:
            try:
                player2_turn = int(input("Player2: Choose a spot based on the correlating number from the diagram above: "))
            except:
                print("THAT'S NOT A NUMBER!!!")
            else:
                if player2_turn < 0 or player2_turn > 9:
                    print("THAT'S NOT AN OPTION!!!")
                else:
                    break


        # PLAYER TWO OUTPUT
        if player2_turn == 1 and top_left == " ":
            top_left = "O"
        elif player2_turn == 2 and top_mid == " ":
            top_mid = "O"
        elif player2_turn == 3 and top_right == " ":
            top_right = "O"
        elif player2_turn == 4 and mid_left == " ":
            mid_left = "O"
        elif player2_turn == 5 and mid_mid == " ":
            mid_mid = "O"
        elif player2_turn == 6 and mid_right == " ":
            mid_right = "O"
        elif player2_turn == 7 and bottom_left == " ":
            bottom_left = "O"
        elif player2_turn == 8 and bottom_mid == " ":
            bottom_mid = "O"
        elif player2_turn == 9 and bottom_right == " ":
            bottom_right = "O"
        else:
            print("YOU FORFEIT YOUR TURN FOR CHOOSING A SPACE THAT WAS TAKEN UP!")

        # DRAW THE BOARD
        gameBoard()
"""
        
