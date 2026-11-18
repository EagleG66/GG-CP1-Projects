# GLENN GUDMUNSON order up

from datetime import datetime as dt

print("\033[H\033[J", end="")

menu = {
    "Main Courses": {
        "Chicken Nuggets": 4.25,
        "Burger": 5.75,
        "Chicken Strips": 4.75,
        "Salad": 5.25
    },

    "Sides": {
        "Waffle Fries": 3.25,
        "Ice Cream": 2.00,
        "Mac & Cheese": 2.75,
        "Onion Rings": 3.50
    },
    "Drinks": {
        "Dr. Pepper": 2.50,
        "Root Beer": 2,
        "Sprite": 1.75,
        "Water": 0
    }
}


print("Hello! Welcome to Chick-fil-a! We are now implementing a \"Chicken Hour\" where everything is 50\% \off from 9:00am to 10:00am")

print("Here is the menu:")

for food in menu.keys():
    print(f"\n{food}")
    for item in menu[food]:
        print(f" - {item}")



while True:
    try:
        main_course = input(f"\nWhich main course would you like: ").title()
    except:
        print("That is not an option. Please try again.")
    else:
        if main_course in menu["Main Courses"]:
            break
        else:
            print("That is not an option. Please try again.")

while True:
    try:
        side1 = input(f"\nWhich side would you like for your first side: ").title()
    except:
        print("That is not an option. Please try again.")
    else:
        if side1 in menu["Sides"]:
            break
        else:
            print("That is not an option. Please try again.")


while True:
    try:
        side2 = input(f"\nWhich side would you like for your second side: ").title()
    except:
        print("That is not an option. Please try again.")
    else:
        if side2 in menu["Sides"]:
            break
        else:
            print("That is not an option. Please try again.")


while True:
    try:
        drink = input(f"\n\nWhich drink would you like: ").title()
    except:
        print("That is not an option. Please try again.")
    else:
        if drink in menu["Drinks"]:
            break
        else:
            print("That is not an option. Please try again.")





total = menu["Main Courses"][main_course] + menu["Sides"][side1] + menu["Sides"][side2] + menu["Drinks"][drink]

print(f"Your order has the following items:\n - {main_course}\n - {side1}\n - {side2}\n - {drink}\nYour total comes to ${total}")

print("\nI threw in 6 chick-fil-a sauces for you... My pleasure")






