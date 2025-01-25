class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance. Try a smaller amount.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

def display_menu():
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

def main():
    atm = ATM(1000)  
    while True:
        display_menu()
        try:
            choice = int(input("Please choose an option (1-4): "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter deposit amount: $"))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter withdrawal amount: $"))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")
main()

