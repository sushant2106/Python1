# def add(x,y):
#     print(a+b)

# def sub(a,b):
#     print(a,b)

# def mul(a,b):

#     print(a,b)


# a=15
# def f1():
#     global a
#     a=10
#     print("f1:",a)

# def f2():
#     a=11
#     print("f2",a)
# def f3():
#     print("f3:",a)

# f3()
# f1()
# f2()
# f3()

a=10
def f5():
    a=20
    print(a)
    print(globals()['a'])
    # print(globals())

def f6():
    print(a)

f5()
f6()

