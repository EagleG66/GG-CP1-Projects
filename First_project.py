#Glenn Gudmunson FIRST PROJECT
import math
import time

#a = int(input("What is A? "))
#b = int(input("What is B? "))
#c = int(input("What is C? "))

#answer1 = -b + math.sqrt(b^2 -4*c*a)/2*a
#answer2 = -b - math.sqrt(b^2 -4*c*a)/2*a

#print("The answers are " + answer1 + " and " + answer2)

x = 0
y = 0
running = True

while running:
    print(y + ":" + x)

    if x >= 60:
        x = 0
        y +=1


    x+=1
    time.sleep(1)


    