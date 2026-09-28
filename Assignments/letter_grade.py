# GLENN GUDMUNSON letter grade

while True:
    try:
        percent = float(input("What percentage do you have in your class: "))
    except:
        print("THAT'S NOT A NUMBER!!!")
    else:
        if percent > 100 or percent < 0:
            print("IT IS IMPOSSIBLE FOR YOU TO HAVE THAT GRADE!!!")
        else:
            break

if percent >= 93:
    grade = "A"
elif percent >= 90:
    grade = "A-"
elif percent >= 87:
    grade = "B+"
elif percent >= 83:
    grade = "B"
elif percent >= 80:
    grade = "B-"
elif percent >= 77:
    grade = "C+"
elif percent >= 73:
    grade = "C"
elif percent >= 70:
    grade = "C-"
elif percent >= 67:
    grade = "D+"
elif percent >= 63:
    grade = "D"
elif percent >= 60:
    grade = "D-"
else:
    grade = "F"

print(f"You have a {grade} in your class")