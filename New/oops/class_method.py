class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print(f'{name} is legs {cls.legs}')

    

Animal.walk('Dog')
Animal.walk('Cat')

#To track no of obeject is created in class

class Test:
    count=0

    def __init__(self):
        Test.count+=1
     
    @classmethod
    def nofobject(cls):
        print('The no of object:',cls.count)
   

    def check(self):
        print(Test.count)
    
t1=Test()
t2=Test()

Test.nofobject()
t3=Test()
t4=Test()
t5=Test()

Test.nofobject()

t1.check()


class DurgaMath:
    
    @staticmethod
    def add(x,y):
        print("The Sum:",x+y)
    
    @staticmethod
    def prod(x,y):
        print("The product:",x*y)

    @staticmethod
    def average(x,y):
        print("The average:",(x+y)/2)
    


DurgaMath.add(10,20)
DurgaMath.prod(10,20)
DurgaMath.average(10,20)


#if you are not using self and any decorator 
#still itsconsider it as static 

#class method and static method are different 


#instance method -> self
#static method 
#class method



