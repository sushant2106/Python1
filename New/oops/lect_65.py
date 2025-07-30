class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def display(self):
        print('name:',self.name)
        print('Your marks are:',self.marks)

    def grade(self):
        if self.marks>=60:
            print('you got first')
        
        else:
            print('You are..')

        
n=int(input('Enter no of studemt:'))

for i in range(n):
    name=input('Enter the stident name:')
    marks=int(input('Enter the marks:'))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()


