class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
            return s
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        
        return sum
    

s1=Student(30,50)
print(s1.sum(10,20,98))




##############
class A:
    def show(self):
        print('A show')


class B(A):
    def show(self):
        print('I am in B')


a1=B()
a1.show()

    
