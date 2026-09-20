def check_balance():
    global Balance
    print(f"Your current Balance is ${Balance}.")
    print("=============================")

def deposit_balance():
    amt=int(input("Enter Deposit Amount: "))
    print("=============================")
    if amt<0:
        print("You cannot deposit a negative amount. Enter a positive amount.")
    elif amt>0:
        global Balance
        Balance+=amt
        print(f"Transaction Complete successfully! Amount ${amt} Deposited.")
    else:
        print("Please enter a valid amount. Try Again.")


def withdraw_balance():
    amt=int(input("Enter Withdraw Amount: "))
    print("=============================")
    global Balance
    if Balance<amt:
        print(f"Transaction Denial! Your current Balance is lower than {amt}. ")
    elif Balance>amt:
        Balance-=amt
        print(f"Transaction Complete successfully! Amount ${amt} Withdrawn.")
    else:
        print("Please enter a valid amount. Try Again.")

# def check_kyc(**docs):
#
# kyc_documents = 0
Balance = 0
if __name__ == "__main__":
    print("=============================")
    print("Welcome to Simple Bank App")
    print("=============================")
    print()
    while True:
         print("1. Check your Balance")
         print("2. Deposit Amount")
         print("3. Withdraw Amount")
         print("4. Exit")
         choice = input("Enter your choice(1-4): ")
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
             print("Please enter a valid choice. Try Again")
