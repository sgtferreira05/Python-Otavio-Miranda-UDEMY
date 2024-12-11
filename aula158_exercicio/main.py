# Exercice with Abstration, Inheritance, Encapsulation and Polymorphism;
# Create an extremely simple banking system with customers, accounts and a bank.The idea is that a customer has an account(savings or checking) and can withdraw or deposite into that account. Checking accounts have an additional limit.

"""
Account (ABC)
    SavingAccount
    CheckingAccount

Person ()
    Customer
        Customer -> Account

Bank
    Bank -> Client
    Bank -> Account

    

Tips:
Create a customer class that inherits from the person class (Inheritence)
    Person has a name and age (with getters)
    Customer has a account(SavingAccount and CheckingAccount class aggregation)
Create SavingAccount and CheckingAccounts classes that inherits from Account
    CheckingAccount has to have an additional limit
    Accounts have a branch, account number and balance
    Accounts must have a deposite method
    Account(Super Class) must have an abstrate withdraw method (Abstration and polymorphism - the subclasses that implement the withdraw method)
Creat Bank class to aggregate customer and account classes(Aggregation)
Bank will be responsible to authenticating the customers and accounts in the following way:
    Bank has accounts and customers(Aggregation)
    * Check if the branch belongs to that bank
    * Check if the customer belongs to that bank
    * Check if the account belongs to that bank
Withdrawls will only be allowed if the customer sucessfully completes the bank's authentication process(describe above)

    
"""

# def SavingAccount(self, branch, accountNumber, balance):
#     self.branch = branch
#     self.accountNumber = accountNumber
#     self.balance = balance
    
# def CheckingAccount(self, branch, accountNumber, balance):
#     self.branch = branch
#     self.accountNumber = accountNumber
#     self.balance = balance

import Account



class checkingAccount(Account):
    def withdraw():
        ...

class savingAccount(Account):
    def withdraw():
        ...

class Person:
    def name(self, name):
        self.name = name
    def age(self, age):
        self.age = age

class Customer(Person):
    ...

class Bank:
    ...