#GLENN GUDMUNSON user signin

#credentials
username = "EagleG66"
password = "123456789"

# credentials check
while True:
        
    username_input = input("What is your username: ")
    password_input = input("What is your password: ")

    if username == username_input and password == password_input:
        print("You have officially signed in!!!")
        break
    else:
        print("Invalid credentials! Please try again")