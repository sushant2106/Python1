class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks=marks
    
    def  getMarks(self):
        return self.marks
    


n=int(input('Enter no of studemt:'))

for i in range(n):
    s=Student()
    name=input('Enter the stident name:')
    s.setName(name)
    marks=int(input('Enter the marks:'))
    s.setMarks(marks)

    print('Name:',s.getName())
    print('Marks',s.getMarks())
    print()

    


    