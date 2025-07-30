class Student:
    #this is doc string
    ''' self refer the current object '''
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        x=10 #variable declare inside method is callled
        #local variable
        print(self.name ,self.rollno,self.marks)

    

s=Student('Ram',23,95)
 #s is ref variable pointing to Student object()

print(s.name,s.rollno,s.marks)
print(s)

#object creation and accessing

#constructor to perform initializatoion
#initialization of object 
#to provide value to instance variable
#instance or object value

s2=Student('Shyam',2,89)
s2.display()

print(s2.__doc__)
#help(Studnet)

print('hello %s' %(s2.name))


#static variable 

class Student1:
    cname='DurgaSoft' #class level variable static variable

s=Student1()
s1=Student1()
print(s.cname)
print(Student1.cname)

s1.cname='Changing'
print(s1.cname)
print(s.cname)






