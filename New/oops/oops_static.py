# class Test:
#     a=10
#     def __init__(self):
#         self.b=11
    
#     def m1(self):
#         self.c=12

#     @classmethod
#     def m2(cls):
#         cls.d=40
#         Test.f=90
    
#     @staticmethod
#     def m3():
#         Test.g=90

    
# t=Test()
# t.d=19

# print(Test.a)


# print(t.__dict__)
# print(Test.__dict__)

# class Test:
#     x=10
#     def __init__(self):
#         self.y=20


# t1=Test()
# t2=Test()

# t1.x+=1
# t2.y+=1

# print('t1:',t1.x,t1.y)
# print('t2:',t2.x,t2.y)
# print('Test:',Test.x)


# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
    
#     def m1(self):
#         self.a=888
#         self.b=999


# t1=Test()
# t2=Test()

# t1.m1()
# print(Test.a)
# print(t1.a,t1.b)
# print(t2.a,t2.b)


class Test:
    a=10
    def __init__(self):
        self.b=20
        self.a=80
    
    
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999



t1=Test()
t2=Test()

t1.m1()
t2.m1()
print(Test.a,Test.b)
print(t1.a,t1.b)
print(t2.a,t2.b)

