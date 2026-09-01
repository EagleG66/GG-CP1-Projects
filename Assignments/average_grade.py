# GLENN GUDMUNSON Average Grade

while True:
    try:
        class1 = int(input("What percent do you have in your first period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class2 = int(input("What percent do you have in your second period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class3 = int(input("What percent do you have in your third period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class4 = int(input("What percent do you have in your advisory class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class5 = int(input("What percent do you have in your sixth period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class6 = int(input("What percent do you have in your seventh period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break

while True:
    try:
        class7 = int(input("What percent do you have in your eighth period class? "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        break




avg_grade = (class1+class2+class3+class4+class5+class6+class7)/7

print("Your average grade is",round(avg_grade,2))