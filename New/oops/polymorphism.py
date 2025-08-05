#duck typing 

class Pycharm:
    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Compiling,,')




class Laptop:
    def code(Self,ide):
        ide.execute()


ide=MyEditor()

# ide=Pycharm()
lap1=Laptop()
lap1.code(ide)

#Operator overalding 



a=5
b=6

print(a+b)


print(int.__add__(a,b))

#these are called magic method 
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        m1=self.m1 + other.m1
        m2=self.m2 +other.m2
        s3=Student(m1,m2)
        # print(s3)
        return s3
    
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m1+other.m2

        if r1>r2:
            return True
        else:
            return False
    
    def ___str__(self):
        return '{} {}'.format(self.m1,self.m2)


    


s1=Student(50,60)
s2=Student(60,70)
s3=s1+s2
print(s3.m1)

if s1>s2:
    print('S1 will win')
else:
    print('s2 will win')

print(s1)
print(s2)

#
    



