class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    
    #self ref to current object
    def m1(self):
        self.d=40
        Test.e=50
    
    #ref to current class object
    @classmethod
    def m2(cls):
        #cls means pointing to current class
        cls.f=60
        Test.g=85
    
    @staticmethod
    def m3():
        Test.h=70




t=Test()
t.m1()
Test.m2()
Test.m3()
print(Test.__dict__)

print(t.h,t.g,t.d)

