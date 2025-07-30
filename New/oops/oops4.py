class SE:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech


s1=SE('Durga',48,'python')
s2=SE('Pathu',49,'Java')

s1.gf='Sunny'
s2.brand='RC'
s2.brand2='KF'

print(s1.__dict__)
print(s2.__dict__)