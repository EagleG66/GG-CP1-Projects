# GLENN GUDMUNSON Fix Game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:

        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: "))      #<<<<< The runtime error was because if the user types in anything other than a number, it breaks during the game. Nevertheless, I have fixed this problem with a try and except loop.
            except:
                print("That is not a number. Please try again.")
            else:
                if guess < 1 or guess > 20:
                    print("That is not in the specified range. Please try again.")      #<<<<< The logic error was because the program did not check if the guess was a number between 1 and 20. I have fixed this with an if statement inside the try and except loop.
                else:
                    break
        guesses = guesses + 1

        if guess == secret_number:       #<<<<< The syntax errror was because of a missing colon, which wouldn't allow the computer to read the code properly, stopping the game from running entirely
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print(f"Your guesses per round: {scores}")     #<<<<< The Runtime error was because it tried to concatenate something that you can't concatenate. I have fixed this with an f-string

total = 0
for score in scores:
                           #<<<<< The logic error was because it sets total to 0 every iteration, which makes it pointless to add the score to total. This made the average guesses per round incorrect
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(2, average)))      #<<<<< The logic error was because it did not round the average, making it hard for the user to read. 

best_round = scores[0]
for i in range(rounds):           #<<<<< The logic error was because the end of the range didn't include your last two rounds. However, since I switched the -1 to rounds and I deleted the 1 at the beginning so that it includes the first number in the list. If I didn't do that, it would sometimes give you a wrong "best round."
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")