class Test:
    a=10
    def __init__(self):
        #pointing to current object
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)
    

    @classmethod
    def m2(cls):
        #cls means pointing to current cls
        print(cls.a)
        print(Test.a)

    
    @staticmethod
    def m3():
        print(Test.a)


    
t=Test()
print(t.a)
