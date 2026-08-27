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
"""

while True:
    if kb.press_and_release(kb.KEY_DOWN):
        print("WOW")                          

"""

# TIC TAC TOE

top_left = None
top_mid = None
top_right = None
mid_right = None
mid_left = None
mid_mid = None
bottom_left = None
bottom_right = None
bottom_mid = None



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

while True:
    try:
        player1_turn = int(input("Choose a spot based on the correlating number from the diagram above"))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        if player1_turn < 0 or player1_turn > 9:
            print("THAT'S NOT AN OPTION!!!")
        else:
            break


if player1_turn == 1 and top_left == None:
    top_left = "X"
if player1_turn == 2 and top_mid == None:
    top_mid = "X"
if player1_turn == 3 and top_right == None:
    top_right = "X"
if player1_turn == 4 and mid_left == None:
    mid_left = "X"
if player1_turn == 5 and mid_mid == None:
    mid_mid = "X"
if player1_turn == 6 and mid_right == None:
    mid_right = "X"
if player1_turn == 7 and bottom_left == None:
    bottom_left = "X"
if player1_turn == 8 and bottom_mid == None:
    bottom_mid = "X"
if player1_turn == 9 and bottom_right == None:
    bottom_right = "X"
