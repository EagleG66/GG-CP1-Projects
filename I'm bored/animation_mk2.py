import time as tm

design1 = ["@@"]
design3 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","@@"]
design2 = ["@@"]
design4 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","@@"]

progress = 10

while True:

    for i in range(50):

        print(*design1, end="")
        print(*design3)
        print(*design2, end="")
        print(*design4)
        tm.sleep(0.1)
        print("\033[H\033[J", end="")
        design1.insert(0, " ")
        design2.insert(0, " ")
        design3.remove(design3[0])
        design4.remove(design4[0])


    for i in range(50):

        print(*design1, end="")
        print(*design3)
        print(*design2, end="")
        print(*design4)
        tm.sleep(0.1)
        print("\033[H\033[J", end="")
        design1.remove(design1[0])
        design2.remove(design2[0])
        design3.insert(0, " ")
        design4.insert(0, " ")