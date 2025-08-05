class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print(f'{self.name} {self.model} {self.color}')


class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    
    def empinfo(self):
        print('Employee NAME:',self.ename)
        print('Employee number:',self.eno)
        print('Employee Car info')
        self.car.getinfo()

c=Car('Innova','2.5Z','Grey')
e=Employee('Durga',100,c)

#Has a Relation

e.empinfo()

#we are able to call Car class bz 
#Employee having car object 


