import random

deck1 = ["2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs"]


while True:

    input("Press ENTER to begin a new game.")
    print("\033[H\033[J", end="")

    deck2 = deck1

    input("Have player 2 look away while you get your cards. Press ENTER when you are ready.")
    print("\n")

    p1card_hidden = random.choice(deck1)
    deck2.remove(p1card)

    while True:

        p1card = random.choice(deck1)
        deck2.remove(p1card)

        print(f"You drew a {p1card}")
        print("\n")

        while True:
            try:
                new_card = input("Would you like to draw another card?(yes or no): ").lower()
                print("\n")
            except:
                print("You messed up...")
                print("\n")
            else:
                if new_card != "yes" and new_card != "no":
                    print("That is not one of the answers. Please try again.")
                    print("\n")
                else:
                    break
            
        if new_card == "yes":
            pass
        elif new_card == "no":
            break



