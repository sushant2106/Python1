
# # x=0

# # while x >=0:
# #     x=int(input("Enter the Age"))
# #     print(x)


# a,b=10,20
# a,b,c,d=10,20,20,30
# print(c,d)

# print(type(a))

# a=True
# print(a , type(a))

# def f1():print("Good Evening")

# print(f1)

# x=10 if a>b else 20
# x=10.5
# print(type(x))

# # y=float(input("Enter the num"))
# # print(y)

# x=10
# def f1():
#     print("Don")

# from random import *
# print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')


# import keyword

# print(keyword.kwlist)

# a=10
# print(type(a))
# print(id(a))
# a=0B10
# print(a)
# a=0o1111
# print(a)
# a=0XFace
# print(a)



# print(bin(15))
# print(oct(15))
# print(hex(15))
# print(bin(0X1234))

# print(hex(0o123))




# #float data type 

# f=123.45
# print(f)

# f1=1.211e3
# print(f1)

# f2=1.2e100
# print(f2)

# #comples data type
# x=10+2j
# print(type(x))
# y=1.5 +2.3j
# print(y)
# a=0B1111+20j

# print(y.real)
# print(y.imag)

# #bool
# a=True
# b=False
# print(a)
# print(type(a))

# a=True+True
# print(a)

# string='''  oka
# line
# '''
# print(string)

# x=''' Durga sir "pyhton"  class '''
# print(x)

# name='durga'

# print(name[0:-2])

# s='durga'
# print(s*3)
# print(len(s))

# print(int("10"))

# # error ->    print(int("10.5"))

# print(float(10))
# # type error print(float(10+2j))

# print(float(True))
# print(float(0B111))
# # print(float("ten"))
# print(complex(10.23))
# print(complex(2,3))

# print(complex(True))
# print(complex(False))

# # print(complex('OB1111'))

# print(complex("10"))

# # error rint(complex("10","20"))

# print(bool(10))

# print(bool(0.0))
# print(bool(0.8))
# print(bool(1.3))
# print(bool(10+2j))
# print(bool(10))
# print(bool(''))
# print(bool('durga'))

# v1='Sikta'
# v2="Sikta"
# v3="Sikta"

# print(id(v1)) #v1 pointing of obhecjt 
# print(id(v2)) #id will provide adrees of object 

# v2='Bettiah'

# print(id(v2))

# #same object can be used by multiple refrence 
# #memory utilization and peformance

# x=10
# y=10
# # == equal to is -> it will check object address 
# if x is y:
#     print("yes")
# else:
#     print("No")

# a=256
# b=256
# #0 to 256 only 
# print(b is a)


# x=10.0
# y=10.0
# # print(x is y)

# # x=10+2j
# # y=10+2j
# # print(x is y)


# # x=[10,20,30]
# # b=bytes(x) #bytes range from 0 to 256 its immutable 
# # print(b[0])

# # for x in b:
# #     print(x)
# # #b[0]=11 not allowed 

# # for x in b:print(x)

# # #bytearray  is immutable

# # x=[10,20,30,40]
# # b=bytearray(x)
# # b[0]=120
# # print(x[0])
# # for x in b:print(x)


# #list data type 

# #insertion order is preseverd and duplicates are allowed 

# # list=[1,2,3,4]
# # list.append(10)
# # print(list)
# # list.pop()
# # print(list)
# # list.remove(4)
# # print(list)

# # s=[10,"durga",True]
# # print(s*2) # number and list


# # t=(10,"durga",True)
# # print(t)
# # print(t[0:2])

# # # t[0]=100 not mutable 
# # print(t*2)

# # t3=(1,3,[10,20])
# # print(t3)

# # # for i in range(1,20,3):
# # #     print(i)

# # s1={10,20,30,20,10}
# # print(s1)
# # # print(s1[0]) error 

# # s1.add('durga')

# # print(s1)
# # s1.remove(20)
# # print(s1)

# # s=set()  #mutable

# # for i in range(10):s.add(i)

# # print(s)

# # #frozenset   set is mutable and frozenset is immutable 
# # s3={10,20,30}
# # fs=frozenset(s3)

# # print(fs)
# # #[],(),{}
# # #dictionary 

# # #emoty set       s=set()
# # # s1=set{},dic={},list=[],tuple=()
# # dic={
# #     100:'Sachin',
# #     101:'Ram'
# # }
# # print(dic)

# # d2={}

# # d2['RollNo']=213
# # print(d2)

# # l2=[1,2,3,4]
# # b=bytes(l2)
# # print(b)

# # s5={10,29,122}

# # print(s5)

# # s5.add(40)
# # print(s5)
# # s5.remove(10)
# # print(s5)


# # fs=frozenset(s5)

# # print(fs)
# # # fs.add(12)
# # # print(fs)


# # #None means No Value 
# # def lock():
# #     a=10
# #     # return None

# # if lock() is None:
# #     print('Yes')


# # s='durga\nsoftware'
# # print(s)

# # sk='durga\tMaA'
# # print(sk)

# # sk='durga\\ji'
# # print(sk)

# # s="Pyhton by \"Durga\" sir"
# # print(s)

# # sn=" Python by \'durga\' \"sir\" "
# # print(sn)

# # floor division 5//2

# print('Floor',5//2) #floor most nearest ....ceil next nearest number 
# print(5/2)
# print(5%2)
# print(10.5//3)

# # s='durga'+3
# # print(s)

# print('durga'* 3)

# print(3*'durga')

# a=10 #durga
# b=29 #ravi based on alphabetical order 


# print("a>b",a>b)
# print("a<b",a<b)
# print("a>=b",a>=b)
# print("a<=b",a<=b)

# if a == b:
#     print(a)

# elif a>=b:
#     print(b)
# else:
#     print(b)

# print(10>20>3)

# print(10==20==30)
# print(10=='10')
# print(10==10.0)

# a=100 
# b=200

# if a>=100 and b>=300:
#     print(a,b)

# else a>=100 and b>=300

# print( not 10)
# b=True
# print(not b)

# if a & b:
#     print(a)
# else:
#     print(b)

# print(~5)
# print(5>>1)

# x=20 if 10<20 else 30  #ternary 
# print(x)

# print(30 if 5>1 else 40)

# a,b=10,20

# print(a if a>b else b)

# a=int(input("Enter the Number"))
# b=int(input("Enter b"))

# min=b if a>b else a
# print(min)

# a,b,c=10,20,13
# print(a is not b)
# # max=c if a>b and b>a else ()

# a=10
# b=10
# c=20
# print(a is b)
# print(a is not c)

# list1=[10,20]
# list2=[10,20]
# print(id(list1))
# print(id(list2))

# print(list1 is list2) # check address comaprison 
# print(list1 is not list2)
# print(list1==list2 ) #contain comparison


# print(10 in [10,20,30]) 
# print(30  in [20,10,25])
# print(30 not  in [20,10,25])

# import math 
# print(math.sqrt(15))
# print(math.pi)
# from math import sqrt,pi
# import pandas as pd
# from math import *
# print(ceil(2.45))
# print(floor(2.45))

# from math import * 
# r=int(input("Enter Radius:"))
# area=pi*r**2
# print(area)

# import math
# print(math.sqrt(24))

# print("the sum,",int(input("Enter the 1st No"))+int(input("Enter 2nd Number")))

# x=10 if 10>20 else 20
# print(x)

# married=bool(input("Are you married"))
# print(married)

#how to read multiple value in single line

# x=[int(x) for x in input("eNTER 2 no:").split(",")]
# print(x)

# a,b=[x for x in input("Enter the Multi No").split(" ")]

# print(a,b)
# import math

# x,y=[float(x) for x in input("Enter the float:").split()]
# print("Sum",math.floor(x+y))


#eval() always take string 

# x=eval("10+20+30")
# print(x)

# ex=input("Enter some expression:")

# print("result",eval(ex))

# x=eval(input("Enter some :"))
# print(type(x))

# li=[1,2,3]
# print(type(tuple(li)))
# a,b,c=[eval(x) for x in input("Enter 3 value").split(":")]
# print(a,b,c)

# void main(String []args)

# argv==>list type sys module
# import sys 
# from sys import argv

# print(len(argv))

# for x in argv:
#     print("yes",x)

# import sys

# print("This is the name of the program:", sys.argv[0])
# print("Number of elements including the name of the program:", len(sys.argv))
# print("Number of elements excluding the name of the program:", len(sys.argv) - 1)
# print("Argument List:", str(sys.argv))

# from sys import argv

# # args=argv[1:]
# # print(args)

# add=0
# n=len(argv)
# print("yes",n)

# print("yes")
# print("Good\n")
# # print()
# print("How are ")
# print("durga"+"Software")
# a,b,c=10,20,30
# print(a,b,c) # by default space 
# print(a,b,c,sep=',')

# #next data printed with seprate line 
# print("Hello",end='')
# print("student",end='')
# print("VeryEasy",end='')

# list=[10,20,30,40]

# t=(10,20)
# s={10,20,30}

# print(list,sep=':')
# print(t,end=':')
# print(s,':')

# a,b,c=10,20,30
# print("a value is %i" %a)

# print("a value is %i and b value is %i" %(a,b))
# name='rAM'

# print('name of perosn %s and list %s' %(name,list))

# print(f'{name}')

# print('hello {}'.format(name))

# m=2.3

# print("Show the float value %f" %(m))

# x,y,z=[ eval(x) for x in input('Enter the no').split(':')]
# print(x)
# # from sys import argv

# x=True

# y=0
# if y!=0:
#     print(y)
# else:
#     print(not x)

# for i in range(10,1,-1):
#     print(i)

# x=10

# while x>=0:
#     print(x,end=':')
#     x-=1

# name=""

# if name==True:
#     print('yes')
# else:
#     print('No')

# a,b=[eval(x) for x in input("eNTER ONLY NO:").split(':')]

# if a>0 and b>=0:
#     print(a)

# else:
#     print(b)

# for i in range(5):
#     for j in range(i+1):
#         print('*',end='') 
#     print()

# for i in range(1,5):
#     print(i)

# cart=[10,20,600,60,70,90,7]
# for item in cart:
#     if item>500:
#         print("sorry we can't")
#         break
#     print("Process item is %i" %(item))

# for i in cart:
#     if i%2==0:
#         continue
#     else:
#         print(i)


# x=10
# print(x)
# del x

# print(x)

# s='Kar'
# del s[1]
# print(s)

# x=10
# y=20
# z=30

# del x,y
# z=None
# print(z)

# s1=10
# s2=10
# s3=10

# print(id(s1))
# print(id(s2))

# del s1
# print(s2)

#varibale and its object is also not required

#want varibale and don't want Corresponding object then S1=None

# from sys import argv

# print(argv)

# x=10
# print('Enter the no %i' %(x))

# s=input("Enter the string:")
# print(s[1:len(s):2])
# print(s[0])
# # i=0

# print(s[::])

# print(s[0:len(s)])

# for x in s:
#     print("Show the character %s and %i" %(x,len(s)-i))
#     i+=1Q


# print(s[-(len(s)-1):-1])



# print(s[-1:-len(s):-1])

# print(s[1:6:-2])

# lis=[12333,33]
# print(len(lis))


# s='abcdefg'

# print(s[:0:-1])
# print(s[0::-1])
# print(s[-1::-1])

# s=input("Enter the Name:")
# i=len(s)-1
# while i>=0:
#     print(s[i],end=":")
#     i-=1

# print()

# x,y,z=10,20,30

# print(x,y,z,sep=',')

# x="mississippi"


# y="Durga Software Solution"

# s=input("Enter Main String:")
# subs=input("Enter the Substring to search:")


# if subs in s:
#     print(subs)

# else:
#     print("Not ")

#== !=
#> >= < <=


# x="durga"
# y='ram'

# # == content comparison 

# if y>=x:
#     print("X %s" %x)

# elif x==y:
#     print("x and y %s and %s" %(x,y))

# else:
#     print("x")

# s1="ram"


# s1=input("Enter the String:")
# s2=input("Enter the string2:")

# if s1==s2:
#     print(s1)

# elif s1>s2:
#     print(s1)
# else:
#     print(s2)

# l1=["A","B"]
# l2=["A","B"]
# print(l1 is l2)
# print(id(l1))
# print(id(l2))
# l3=l2
# print(l1==l2)
# print(l1 is l2)
# print(l3 is l2)
# a=10
# b=10
# print(a is b)

city=input("Enter theCity Name:")
list=["Hyderabad","Delhi","Mumbai"]

#lstrip(),rstrip(),"strip()"
if city.strip() in list:
    print(city)

else:
    print("Not available")

# from list_ import f2

# f2()

