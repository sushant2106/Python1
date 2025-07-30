print("Hello..I am module1....")

#finding member of module

#dir() ->list of current module

# x=10
# y=20

# def f1():
#     print("Hello..")


# print(dir())
# import imp
# print(dir(imp))

# # print(__builtins__)
# # print(__doc__)
# # print(__loader__)
# print(__name__)
# # print(__file__)

# def f1():
#     if __name__ == '__main__':
#         print("The code exhausted")
#         print(__name__)
#     else:
#         print(__name__)

import math

print(dir(math))
print(math.sqrt(10))
print(math.ceil(1.8))
print(math.floor(22.45))

print(math.fabs(-10.6)) #absilute value
print(math.fabs(10.6))

print(math.pi)
print(math.pow(2,3))

from  random import *
# print(dir(random))

for i in range(10):
    print(random())
    print(randint(1,100))
    print('Iam float',uniform(1,10))

#randrange(start,stop,step)

print('I am range',randrange(1,100,5))

#choice() function

list=['ram','shyam','ghanshyam']
# lis1={}

for i in range(10):
    print(choice(list))


#otp digit


for i in range(10):
    # print(randint(0,6)*6,sep='')
    # print(randint(0,10),randint(0,10))
    print(randint(0,10),chr(randint(65,65+25)),randint(0,10),sep='')




    

#python 3.3 onwards






  
   




