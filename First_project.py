#Glenn Gudmunson FIRST PROJECT
import math
import time


#MATH
"""
a = int(input("What is A? "))
b = int(input("What is B? "))
c = int(input("What is C? "))

answer1 = -b + math.sqrt(b^2 -4*c*a)/2*a
answer2 = -b - math.sqrt(b^2 -4*c*a)/2*a
str1 = str(answer1)
str2 = str(answer2)

print("The answers are " + str1 + " and " + str2)

"""
#TIMER

x = 1
y = 0
running = True


while running:

    strY = str(y)
    strX = str(x)

    if x >= 10:
        print(strY + ":" + strX)
    else:
        print(strY + ":0" + strX)

    if x <= 0:
        x = 59
        y -=1

    if y <= 0:
        x = 0
        y = 0


    x += 1
    time.sleep(1)


    