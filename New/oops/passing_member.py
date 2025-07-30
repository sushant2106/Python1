class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print("Emplye no:",self.eno)
        print("Employee Name",self.ename)
        print("Employe Salary:",self.esal)




class Test:
    def modify(emp):
        emp.esal+=1000
        emp.display()


#passing object to another class as argument 
e=Employee(100,'Durga',10000)
Test.modify(e)


#Inner classes/nessted class

class Outer:
    class Inner:
        





