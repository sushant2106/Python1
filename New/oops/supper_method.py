class X:
    a=10
    def m1(self):
        print('Parent class instance method')
    
    @classmethod
    def m2(cls):
        print('Parent class Staticmehtod')
    
    @staticmethod
    def m3():
        print("Parent static Method")

    def __init__(self):
        self.b=888
        print('Parent Constructor..')
  

class Y(X):

    def __init__(self):
        #   super().__init__()
        print('child constructor...')
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print(super().a)
        print(Y.a)
    

y=Y()