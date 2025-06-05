#BankAccount class with deposit and withdraw methods.
import math
class BankAccount:
    def __init__(self, fname, lname, pnumber, email, accountNumber):
        self.fname = fname
        self.lname = lname
        self.pnumber = pnumber
        self.email = email
        self.minaccountbalance = 1000
        self.creditcardbill = 0
        self.accountNumber = accountNumber
        self.currentBalance = 2000
        self.branch = "New York"

    def deposit(self, depositAmount):
        self.currentBalance = self.currentBalance + depositAmount

    def credit(self, creditAmount):
        self.currentBalance = self.currentBalance - creditAmount

    def accountInfo(self):
        print(f"Name: {self.fname} {self.lname}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Phone: {self.pnumber}")
        print(f"Email: {self.email}")
        print(f"Min Balance: ${self.minaccountbalance}")
        print(f"Current Balance: ${self.currentBalance}")

    def __str__(self):
        return f"Name: {self.fname} {self.lname} Current Balance: ${self.currentBalance}"

myBankAccount = BankAccount("divya","avvaru",779491365, "divya@email.com", 13023566)
myBankAccount.accountInfo()
print("----------")
#deposit
myBankAccount.deposit(1024)
myBankAccount.accountInfo()
print("----------")
#credit
myBankAccount.credit(365)
myBankAccount.accountInfo()
print(myBankAccount)



    