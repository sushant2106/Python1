
# def decor(func):
#     def inner(name):
#         if name=='Sunny':
#             print('Hello SUnny..')
        
#         else:
#             func(name)
    
#     return inner


# # @decor
# def wish(name):
#     print(name,"Good Morning")

# decorfunction=decor(wish) #eiter @ or like this



# # wish('Durga')
# # wish('Ravi')
# # wish('Sunny')


# # def outer():
# #     def inner():
# #         print("I am ineer func")
    
# #     print("First execute Outer func")
# #     return inner


# # x=outer()
# # x()






# # def outer():
# #     print("yes Make it alias function ..")

# # x=outer
# # x()


# # from functools import reduce
# # li=[10,20,13,14,17]

# # print(list(filter(lambda x: x%2==0,li)))
# # print(list(map(lambda x: x+2 ,li)))
# # print(reduce(lambda x,y:x+y,li))
# # print(reduce(lambda x:x+2,li))



# def decor(func):
#     def inner(name):
#         # print(f'Inner NaME IS {name}')
#         # func(name)
#         if name=='Sunny':
#             print("Hello sunny bad morning")
#         else:
#             func(name)
    
#     return inner




# # @decor
# def wish(name):
#     print(f'I am wish function {name}')



# # wish('RAM JI')

# dec=decor(wish)
# dec('Sunnay')
# dec('ram ji')

# #which take another function as input


# def smartdiv(func):
#     def inner(a,b):
#         if b==0:
#             print("B is zero")
#             return
#         else:
#             return func(a,b)
#         # return  a/b if b>0 else 0
    
#     return inner

# @smartdiv
# def division(a,b):
#     return a/b

# division(10,0)


def decor1(func):
    def inner(name):
        print("first Decor fucntion ")
        func(name)
    return inner

def decor2(func):
    def inner(name):
        print("Second decor extension")
        func(name)
    return inner


@decor2
@decor1
def wish(name):
    print(f"I am real func {name}")


wish('durga ji')
# wish("Ram ji")



def decor4(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor3(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor3
@decor4
def num():
    return 10

print(num())




























