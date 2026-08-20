#Glenn Gudmunson FIRST PROJECT
import time

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


#math homework
def multiply(num1,num2):
    global answer
    correct_answer = num1 * num2
    str_num1 = str(num1)
    str_num2 = str(num2)
    answer = input("What is " + str_num1 + " x " + str_num2)
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are wrong!")

multiply(2,2)


    