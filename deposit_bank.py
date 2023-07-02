
import csv

class customerdeposit:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance += amount
           
            print(f"deposited successful.  balance: {self.balance}")
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

            for row in rows:
                if row[0] == fullpath:
                   row[-1] = str(self.balance)
                   break

            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)
        else:
            print("Insufficient funds.")

    @staticmethod
    def load_balance_from_csv(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            balance = float(next(reader)[-1])
            return balance
   

try:
    # Create a file name based on pancard number
    fullpath = input("Enter your pancard no.: ")
    filename = fullpath + ".csv"

    # Load the balance from the CSV file

    balance = customerdeposit.load_balance_from_csv(filename)

    # Create an instance of the  BankCustomer class
    account =  customerdeposit(balance)

    # Make a withdrawal
    deposit_amount = float(input("Enter your deposit amount: "))
    account.withdraw(deposit_amount)

except Exception as e:
    print("Kindly check all the details, and Try Again!!")
