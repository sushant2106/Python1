#access modifier 

class Person:
    def __init__(self,name,age):
        self.__name=name
        # self.__age=age

        self._age=age #protected

    def display_info(self):
        print(f'{self.__name} and {self._age}')
    

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def disp(self):
        print(f'age is {self._age}')




# p=Person("Krish",'32')
# # print(p.__name) can't access 
# #dir(p)
# print(p._age)

s=Student('Ram',25)
s.disp()
s.display_info()


#method overloading 

class Test:
    def m1(self,*a):
        total=0
        for x in a:
            total+=x
        print('the sum:',total)

t=Test()
t.m1(10,20,30)

x={'name':'shyam'}

# for i,j in x.items():
#     print(j)

#constructor overloading
class Test1:
    def __init__(self):
        print('Noa rg construct')
    
    def __init__(self,a):
        print('one-arg constructor')
    def __init__(self,a,b):
        print('Two-arg')

t1=Test1(10,20)


