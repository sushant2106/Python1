class A(object):
    
    def __init__(self,a):
        self.a=a
        print(a)
        
    def __call__(self):
        print('{self.a} is hum')
        


obj=A(4)

obj() #obj.__call__()

# print(A.__call__(4))