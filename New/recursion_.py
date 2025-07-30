def factorial(n):
    if n==0:
        result=1

    else:
        result=n*factorial(n-1)
    return result

print(factorial(4))


#Anynomous function   

#Without name ... nameless function

#instant use(only one time usgae)



# def squeareIT(n):
#     return n*n

s=lambda n:n*n
print(s(4))

# lambda input:expression
s=lambda x: x**5
print(s(4))

s=lambda a,b:a+b

print(s(3,4))

s2=lambda a,b: a if a>b else b
print(s2(10,20))



#function as argument 


def add(x,y):
    return x+y

s3=lambda a,b: a if a>b else 15

add(s3(10,12),4)

#filter map reduce

#syntax filter(function,sequence)

def iseven(x):
    return x%2==0

l=[0,5,10,15,20,25]

output=list(filter(iseven,l))

print(output)

output2=list(filter(lambda x:x%2==0,l))

print(output2)

out_odd=list(filter(lambda x:x%2!=0,l))
print(out_odd)

# add_list=list(filter(lambda x:x+2,l))
# print('add_list',add_list)

#Map Function

def double(x):
    return 2*x
l3=[1,2,3,4,5]

l4=list(map(double,l3))

print(l4)

l5=list(map(lambda x:x*2,l3))
print(l5)

#passing two sequence
l6=list(map(lambda x,y:x*y,l4,l5))
print(l6)



# s3=lambda x: x**3

# print(s3(7))

#Reduce 
l10=[10,20,30,40,50]
from functools import reduce

result=reduce(lambda x,y:x+y,l10)
print(result)


# function aliasing 

def wish(name):
    print(name)

greeting=wish
print(id(wish))
print(id(greeting))

greeting('ram')
wish('shyam')

#nested function

def outer():
    print("outerfunction started")
    def inner():
        print("Inner function call")

    inner()

outer()


def f1():
    def inner(a,b):
        print(a+b)
        print((a+b)/2)

    inner(10,20)
    inner(20,30)
    inner(40,50)

f1()

def outer2():
    print("OUTER Fun..")
    def inner():
        print("inner function execution")
    print("outer function returnin inner func")
    # return inner()
    return inner

print('Hum Chal rhe hai')
# f1=outer2()
# print(f1)

f1=outer2() #function can return another function
f1()

#f1=outer2() return value asign to f1





#function decorator





