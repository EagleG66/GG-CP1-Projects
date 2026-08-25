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

kb.is_pressed()
    