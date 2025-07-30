class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def display(self,a):
        self.x=a
        print(f'name is {self.name}')
        print(f'Roll no: {self.rollno}')
        print(f'Student Marks: {self.marks}')



s1=Student('Durga',101,90)
s2=Student('Ram',102,95)

print(s1.__doc__)
print(s1.name)
s1.display(10)
#now no if instance
s2.display(3)
print(s1.__doc__)

###################
s2.name='Shyam'
print(s2.name)

print('How s2')
s2.display(4)

##################
print(s1.__dict__)
s1.x=14
print(s1.__dict__)
print('########### I am s2')
print(s2.__dict__)

#we can add instance variable 
s1.c=40
print('########### I am s1 after new instance added')
print(s1.__dict__)


print('########### I am s2 after new instance added')
print(s2.__dict__)


    