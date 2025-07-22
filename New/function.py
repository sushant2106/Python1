# def wish():
#     """ The function written by durga sir"""
#     print("Hi..")
#     return 2,3


# a,b=wish()

# print(a)

# def cal(a,b):
#     sum=a+b
#     sub=a-b
#     div=a/b

#     return sum,sub,div


# t=list(cal(30,20))
# print(type(t))

# #key value argument

# def f1(name,msg):
#     print("Hello",name,msg)


# f1(name='Durga',msg='Good Morning')

# #pos and key argument


# def f2(name,msg):
#     print("Hello",name,msg)


# f2('Durga',msg='Good Morning') #positional argument shoudl first always 


# #default argument

# def wish(name="Guest",msg="Good Morning"):
#     print(name,msg)

# wish("Ram ji")
# # wish()

# def f2(marks,age,name="Guest",msg="Good Morning"):
#     print(name,age,marks,msg,sep=':')

# f2("Durga","Good",22,marks=100)




# def f3(msg,name="Guest"):pass


# f3(msg='ram')

#varibale length argument

# def sum(*n):  #* any no of argument
#     for x in n:
#         print(x,end=':')
#     print()
#     # print("Var-arg function")

# sum()
# sum(10)
# sum(10,30)
# sum(10,20,30)

#n is tuple internally

def sum(*n,name):
    result=0
    for x in n:
        result+=x
    print(name,result)

sum(name="Ram")
sum(10,name="Shiva")
sum(10,20,30,name="Pavan")



def display(**kwargs):
    print("Record Infomration:..")
    for k,v in kwargs.items():
        print(k,"....",v)



#keyword varibale argument

display(name='Durga',marks=100,age=48,area='Sikta')
display(name='Durga',w1='Sikta',w2='Ramnagr',w3='Narkatiganj')




