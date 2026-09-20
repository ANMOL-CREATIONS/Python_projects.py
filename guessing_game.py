import random


print("Hi! Welcome to the Number Guessing Game!")
print("You have 7 chances to guess the number.\n")


# Get valid lower and upper bounds
while True:
    try:
        low = int(input("Enter the Lower Bound: "))
        high = int(input("Enter the Upper Bound: "))

        if low >= high:
            print("Lower Bound must be less than Upper Bound. Try again.\n")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")


# Generate a random number
number = random.randint(low, high)

# Game settings
max_attempts = 7
attempt = 0


print(f"\nGuess the number between {low} and {high}.")
print(f"You have {max_attempts} attempts. Good luck!\n")


# Main game loop
while attempt < max_attempts:

    try:
        guess = int(input(f"Attempt {attempt + 1}/{max_attempts} - Enter your guess: "))

    except ValueError:
        print("Invalid input! Please enter a whole number.\n")
        continue

    attempt += 1

    if guess == number:
        print(
            f"\nCongratulations! 🎉 You guessed the correct number "
            f"{number} in {attempt} attempts."
        )
        break

    elif guess > number:
        print("Too high! Try a lower number.\n")

    else:
        print("Too low! Try a higher number.\n")


else:
    print(
        f"\nSorry! You've used all {max_attempts} attempts. "
        f"The correct number was {number}."
    )

print("\nThanks for playing!")
