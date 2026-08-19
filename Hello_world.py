# GLENN GUDMUNSON Hello World
import time

startZ = int(input("What hour is it?"))
startY = int(input("What minute is it?"))
print("I have now started the clock")

x = 0
y = startY
z = startZ
colon1 = None
colon2 = None
running = True

while running:

    strY = str(y)
    strX = str(x)
    strZ = str(z)

    if x >= 10:
        colon2 = ":"
    else:
        colon2 = ":0"

    if y >= 10:
        colon1 = ":"
    else:
        colon1 = ":0"


    print(strZ + colon1 + strY + colon2 + strX)


    if x >= 59:
        x = 0
        y +=1

    if y >= 59:
        y = 0
        z += 1

    if z > 12:
        z = 1



    x += 1
    time.sleep(1)