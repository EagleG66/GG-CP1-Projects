# GLENN GUDMUNSON Idoit proof

# Name:
first_name = input("WHAT IS YOUR FIRST NAME: ").strip().split()

last_name = input("WHAT IS YOUR LAST NAME: ").strip().split()

full_name = "Hello " + "".join(first_name).title() + " " + "".join(last_name).title()


# Phone number:
while True:
    try:
        phone_num = int(input("What is your phone number: "))
    except:
        print("THAT IS NOT A VALID PHONE NUMBER!!!")
    else:
        break



new_phone = str(phone_num)

newer_phone = new_phone[0:3] + " " + new_phone[3:6] + " " + new_phone[6:10]


# GPA
while True:
    try:
        gpa = float(input("What is your GPA: "))
    except:
        print("THAT IS NOT A VALID GPA!!!")
    else:
        break

print(f"Name: {full_name} \nPhone Number: {newer_phone} \nGPA: {str(round(gpa,1))}")