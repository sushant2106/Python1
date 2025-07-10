class Employe:
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        # self.email=first+'.'+last+'@email.com'
        self.pay=pay
    
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first,self.last)

    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None



    


dev_1=Employe('Corey','Schafer',50000)

# dev_1.first='Sachin'

dev_1.fullname='ram kumar'

# del dev_1.fullname33




print(dev_1.first)
print(dev_1.fullname)
print(dev_1.email)