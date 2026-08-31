class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Input error! Deposit amount must be greater than 0.")
            return False  # Transaction failed
        else:
            self.balance += amount
            return True  # Transaction succeeded

    def withdraw(self, amount):
        if amount <= 0:
            print("Input error! you can not withdraw 0 or less amount.")
            return False  # Transaction failed
        elif amount > self.balance:
            print("Insufficient Balance! please try again.")
            return False  # Transaction failed
        else:
            self.balance -= amount
            return True  # Transaction succeeded

    def display_balance(self):
        print(f"Dear {self.owner}, Your available balance is Rs. {self.balance:.2f}.")

if __name__ =="__main__":
    account1 = BankAccount("Ravi", 1000)
    account1.deposit(500)    
    account1.withdraw(300)
    account1.withdraw(2000)    
    account1.withdraw(-1999)
    account1.deposit(0)
    account1.display_balance()
    account2 = BankAccount("Hari")
    account2.deposit(5000)
    account2.withdraw(3000)
    account2.display_balance()