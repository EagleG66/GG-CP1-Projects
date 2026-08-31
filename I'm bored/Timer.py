import time

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