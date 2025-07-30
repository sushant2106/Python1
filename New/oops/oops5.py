class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40


t1=Test()
t2=Test()

del t1.c

t1.e=50

print('t1',t1.__dict__)
print(t2.__dict__)

# print(t1.c)

#################

class Student:
    ''' school is static variable or class variable '''
    school='Indian Public School'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print('Name',self.name)
        print('School',self.school)
    
    


s1=Student('Ram',1)
s2=Student('Shaym',2)

s1.display()
s2.display()
# s2.school='IPS'
# print('Now access static var')
# print(s1.school)
# print(s2.school)

Student.school='IPS'
s1.name='Sachin'

print('S1',s1.school,s1.name)
print('s2',s2.school,s2.name)







#static variable single copy is created and shared for all object

