def check_balance():
    global Balance

    print(f"Your current balance is ${Balance}.")
    print("=============================")


def deposit_balance():
    global Balance

    try:
        amt = int(input("Enter Deposit Amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        print("=============================")
        return

    print("=============================")

    if amt <= 0:
        print("Deposit amount must be greater than 0.")
    else:
        Balance += amt
        print(
            f"Transaction completed successfully! "
            f"Amount ${amt} deposited."
        )


def withdraw_balance():
    global Balance

    try:
        amt = int(input("Enter Withdraw Amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        print("=============================")
        return

    print("=============================")

    # Reject zero or negative withdrawals
    if amt <= 0:
        print("Withdrawal amount must be greater than 0.")

    # Insufficient balance
    elif amt > Balance:
        print(
            f"Transaction denied! "
            f"Your current balance is ${Balance}, "
            f"which is less than ${amt}."
        )

    # Valid withdrawal, including exact balance
    elif Balance >= amt:
        Balance -= amt
        print(
            f"Transaction completed successfully! "
            f"Amount ${amt} withdrawn."
        )


Balance = 0


if __name__ == "__main__":

    print("=============================")
    print("     Welcome to Simple Bank App")
    print("=============================")

    while True:

        print("\n1. Check your Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        print("=============================")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_balance()

        elif choice == "3":
            withdraw_balance()

        elif choice == "4":
            print("Thank you for banking with us.")
            print("=============================")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 4.")
