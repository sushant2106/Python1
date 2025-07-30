class Test:
    a=10
    def __init__(self):
        self.b=20


t1=Test()
t2=Test()

# t1.a=888 #create new instance variable
t1.b=999
t1.a+=1

print(t1.a,t1.b)
print('##########')
print(Test.a)
print(t1.__dict__)
# print(t1.__dict__)
# print(t2.__dict__)
