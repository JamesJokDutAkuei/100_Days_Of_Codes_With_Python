class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        
        remaining_balance = self.balance - amount
        
        if remaining_balance < 0:
            print("you have insufficient balance to do this transaction")  
        else:
            self.balance -= amount 
           
    
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account_Name: {self.account_name}")
        print(f"balance: {self.balance}")
        


james_account = BankAccount(2227749, "James Jok", 0)

james_account.deposit(450)

james_account.withdraw(400)

james_account.display_account_info()
        
