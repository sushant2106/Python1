class Student:
    ''' document string '''

    def __init__(self):
        self.name='Ram' #instance variable / object variable
        self.rollno=101
        self.mark=90

    def talk(self):
        print('name',self.name)
        print('roll no',self.rollno)
        print('marks',self.mark)



# print(Student.__doc__)
# help(Student)

s1=Student()
# obejct creation Student()
#s1 is refrence variable to point s1
s1.talk()
print(s1.name,s1.rollno)

#self is pointing to current object
#reference variable to current object


class Std:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m

    def disp(self):
        print('Name',self.name)
        print('Marks:',self.marks)



s1=Std()
s1.disp()

s2=Std('Suny',100)
s2.disp()


class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename

    def disp(self):
        print('Name %s' %(self.ename))
        print('Marks',self.eno)


e1=Employee(100,'Ram')
e1.disp()

# e2=Employee(10)
# e2.disp()



