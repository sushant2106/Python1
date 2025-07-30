# class Test:
#     a=10
    
#     @classmethod
#     def m1(cls):
#         del cls.a



# Test.m1()

# del Test.a
# print(Test.__dict__)


#to read static varibale 

import sys


class Customer:
    ''' Customer class with bank operation'''
    bankname='Durgabank'
    
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    
    def deposit(self,amt):
        self.balance+=amt
        print('Balance After deposit:',self.balance)
    
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficent fund')
            sys.exit()
        else:
            self.balance-=amt
            print('Amount after withdraw',self.balance)
  
print(f'Welcome To {Customer.bankname}')

name=input("Enter your name:")
c=Customer(name)
while True:
    print('d-Deposit \nw-withdraw \ne-exit')
    option=input('Choose the option')
    if option=='d' or option == 'D':
        amt=float(input('Enter amount:'))
        c.deposit(amt)

    elif option =='w' or option == 'W':
        amt=float(input("Enter amount:"))
        c.withdraw(amt)

    elif option.lower() == 'e':
        print('Thanks for banking')
        sys.exit()
    
    else:
        print('Invalid option')
        
    
