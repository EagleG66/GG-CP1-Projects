# unit 3 notes

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FUNCTIONS
"""
def birthday(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")
    scare = 154

    return name, scare

user, spook = birthday("Tia")
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   LIBRARY

"""
step1 = "Search for the python library you are looking for"

step2 = "Use the tutorial"

step3 = "import the library"


import turtle as t

t.showturtle()
t.width(10)
t.speed(100)

for i in range(10000):
    t.hideturtle()
    t.forward(i/100)
    t.left(2)
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   NESTED LOOPS

"""
people = ["Hugo", "Daniel", "Glenn", "Logan"]

for i in range(4):
    print("HI", end=" ")
    for person in people:
        if person == people[0]:
            print(person, end="")
        else:
            print(f" and {person}", end="")
    print("\n")

    """

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   DICTIONARIES

car = {
    "make":"Jeep",
    "model":"Wrangler",
    "color":"red",
    "year":1991
}

keys = car.keys()

for key in keys:
    print(f"{key}: {car[key]}")


car["Transmission"] = "Automatic"

print(car["Transmission"])

car.pop("color")

for key in keys:
    print(f"{key}: {car[key]}")

car.items() # Makes a tuple  

print(car.get("model")) # If you use this instead, it won't throw an error  if the item isn't in the dictionary

# make a dictionary inside a dictionary and to call it, you do avatar[fire][iroh]









# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   VOCABULARY

readabilty = "duh..."

modularity = "breaking a big problem into little pieces"

reusabilty = "duh..."

abstraction = "using it without understanding how it works"
