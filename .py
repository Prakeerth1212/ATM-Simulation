import logging
logging.basicConfig(
    filename='atm.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ATM:
    def __init__(self, pin, balance=1000):
        self.correct_pin = pin
        self.balance = balance

    def login(self, entered_pin):
        if entered_pin == self.correct_pin:
            logging.info("Login successful.")
            return True
        else:
            logging.warning("Login failed - incorrect PIN.")
            return False

    def check_balance(self):
        logging.info(f"Balance checked. Current balance: Rs{self.balance}")
        print(f"Your balance is Rs{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        logging.info(f"Deposited Rs{amount}. New balance: Rs{self.balance}")
        print(f"Rs{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            logging.info(f"Withdrew Rs{amount}. New balance: Rs{self.balance}")
            print(f"₹{amount} withdrawn successfully.")
        else:
            logging.error(f"Withdrawal failed. Tried Rs{amount}, Available Rs{self.balance}")
            print("Insufficient balance!")

atm = ATM(pin=2425)

try:
    entered_pin = int(input("Enter PIN: "))
    if atm.login(entered_pin):
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                amt = int(input("Enter amount to deposit: "))
                atm.deposit(amt)
            elif choice == '3':
                amt = int(input("Enter amount to withdraw: "))
                atm.withdraw(amt)
            elif choice == '4':
                print("Thank you for using the ATM!")
                logging.info("Session ended.")
                break
            else:
                print("Invalid choice.")
                logging.warning("Invalid menu option selected.")
    else:
        print("Incorrect PIN. Access Denied.")

except ValueError:
    logging.error("Invalid input (non-numeric PIN or amount).")
    print("Please enter numbers only.")
with open("atm.log", "r") as file:
    log_content = file.read()

print(log_content)
