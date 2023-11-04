# class Investor:

#     def __init__(self,name:str,age:int,cash:float):
#         self.name=name
#         self.age=age
#         self.cash=cash

#     def __repr__(self):
#         return f'My name is {self.name} and age is {self.age}'
    
#     def __eq__(self,other):
#         return self.name ==other.name
    
#     def __lt__(self,other):
#         return self.cash < other.cash


# i1=Investor("JOhn",25,9000)
# i2=Investor("Anna",30,12000)
# i3=Investor("Bob",70,800000)
# i4=Investor("JOhn",25,9000)

# print(i1==i4)

from dataclasses import dataclass,field

@dataclass
class Investor:
    name:str
    age:int
    cash:float = field(repr=False,compare=False)  #default=0

    usn:list[int]=field(default_factory=list)
    # usn:list[int]

    # def __repr__(self):
    #     return "Hello"

i1=Investor("JOhn",25,9000,[1,23])
i2=Investor("Anna",30,12000)
# i3=Investor("Bob",70,800000)
# i4=Investor("JOhn",25,900000)

# print(i1==i4)
print(i1)
print(i2)




