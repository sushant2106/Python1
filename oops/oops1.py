class Employe:
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)



class Developer(Employe):
    raise_amt=10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

        # Employe.__init__(self,first,last,pay)

class Manager(Developer):

    def __init__(self, first, last, pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

        




     

# dev_1=Employe('Corey','Schafer',50000)
# dev_2=Employe('Test','Employee',60000)


# dev_1=Developer('Corey','Schafer',50000)
# dev_2=Developer('Test','Employee',60000)

# # print(dev_1.email)
# # print(dev_2.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

emp1=Developer('Corey','Schafer',50000,'java')
# print(emp1.first)

mgr_1=Manager('Sue','Smith',90000,[emp1])

print(mgr_1.email)





