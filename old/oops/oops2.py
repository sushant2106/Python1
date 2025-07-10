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


    def __str__(self) -> str:
        return self.first
    
    def __repr__(self) -> str:
        return self.last
    
    def __add__(self,other):
        return self.pay+other.pay


dev_1=Employe('Corey','Schafer',50000)
dev_2=Employe('Test','Employee',60000)



# print(dev_1)


print(repr(dev_1))

# print(str(dev_1))

# print(int.__add__(1,2))

# print(str.__add__('a','b'))

print(dev_1+dev_2)