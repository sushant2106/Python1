class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eatdrink(self):
        print('Boryani eating and coldrink')


class SE(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def work(self):
        print('Pyhton coding is somethign like child drinking')


class Studnet(Person):
    pass
class Teacher(Person):
    pass

s=SE('dURGA',48,100,87000)
print(s.name,s.age)
s.eatdrink()


class A:
    x=999
    def m1(self):
        self.x=10

class B(A):
    def m1(self):
        super().__init__()
        self.y=20
        print(super().x)
        print(self.x)
        print(self.__dict__)
    
    # def disp(self):
    #     # print('Ia m disp',self.x)
    #     # print(self.__dict__)
    #     # print(super().x)

b=B()
b.m1()


#instance variable in child class use self 



