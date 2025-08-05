class X:
    a=10
    def m1(self):
        print('Parent class instanc method')
    
    @classmethod
    def m2(cls):
        print('Parent class Staticmehtod')
    
    @staticmethod
    def m3():
        print("Parent static Method")

    def __init__(self):
        self.b=888
        print('Parent Constructor..')
    def __del__(self):
        print('Parent Destructor..')

class Y(X):
    a=777 #from child classes to parent 

    def __init__(self):
        print('child constructor...')
    
    def __del__(self):
        print('Child class')
    @classmethod
    def m2(cls):
        print('Child class Staticmehtod')
    
    @staticmethod
    def m3():
        print("Child static Method")

y=Y()
