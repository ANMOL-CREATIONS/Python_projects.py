"""
write a program to simulate a roll of a die/dice
A die has 6 faces with numbers 1 to 6 written on them
The program should randomly print a number between 1 and 6
"""
import random
print("Welcome to the game of rolling a dice.")
while True:
    choice = input("Press 'enter' to roll the dice or type 'q and enter' to quit. ")
    choice = choice.strip()
    if choice == "q":

        break
    elif choice == (""):
        numbers = random.randint(1, 6)
        print("You Got " + str(numbers))
    else:
        print("Invalid Answers.")
print("THANKS FOR PLAYING THE GAME, GOODBYE!.\nGame Over")
