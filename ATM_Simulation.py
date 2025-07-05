
class atm:
    def __init__(self):
        self.pin = "0000"
        self.balance = 1000
        self.history = []  # ✅ Step 1: Initialize transaction history
        self.menu()

    def menu(self):
        while True:
            user_input = input("""\nEnter the operation you wish to proceed with 
  1. Enter 1 to create pin: 
  2. Enter 2 to check balance: 
  3. Enter 3 to deposit money:  
  4. Enter 4 to withdraw money: 
  5. Enter 5 to view transaction history: 
  6. Enter 6 to Exit: 
""")

            if user_input in ['1', '2', '3', '4', '5', '6']:
                print("I would be grateful to help you")
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            if user_input == "1":
                self.set_pin()
            elif user_input == "2":
                self.check_balance()
            elif user_input == "3":
                self.deposit()
            elif user_input == "4":
                self.withdraw()
            elif user_input == "5":
                self.show_history()
            elif user_input == "6":
                print("Thank you for using the ATM.")
                break

            use_again = input("Do you wish to perform another operation? {Yes/No} ").lower()
            if use_again != 'yes':
                print("Thanks for joining with us.")
                break

    def set_pin(self):
        self.pin = input("Enter your new pin: ")
        print("Pin set successfully.")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is ₹{self.balance}")
        else:
            print("Invalid pin.")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")  # ✅ Step 2: Log deposit
            print("Deposit successful.")
        else:
            print("Invalid pin.")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                self.history.append(f"Withdrew ₹{amount}")  # ✅ Step 2: Log withdrawal
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid pin.")

    def show_history(self):
        temp = input("Enter your pin to view transaction history: ")
        if temp == self.pin:
            if self.history:
                print("\nTransaction History:")
                for transaction in self.history:
                    print(f"- {transaction}")
            else:
                print("No transactions found.")
        else:
            print("Invalid pin.")

user = atm()