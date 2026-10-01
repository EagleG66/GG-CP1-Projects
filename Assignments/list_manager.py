# GLENN GUDMUNSON Shopping List Manager

shopping_list = []

print("You currently have nothing in your list...")

while True:
    action = input("What action you would like to take(add, remove, exit): ")

    if action == "add":
        item = input("What would you like to add to the shopping list: ")
        shopping_list.append(item)
        print(f"Your shooping list now contains:")
        print(*shopping_list)

    elif action == "remove":
        item = input("What would you like to remove from the shopping list: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Your shooping list now contains:")
            print(*shopping_list)
        else:
            print("That item is not currently in the shopping list")

    elif action == "exit":
        print("Your end list looks like this:")
        print(*shopping_list)
        break
    else:
        print("That is not an available action you can take. Please try again")
