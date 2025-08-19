from dataclasses import dataclass

@dataclass
class Person:
    name :str ='Ram'
    age: int =7
    prefession : str | None=None

x=Person('Krish',17,'SE')

print(x.name)


@dataclass
class Rectangle:
    widht:int
    height:int
    color:str='WHITE'



rectangle1=Rectangle(12,14)
rectangle2=Rectangle(13,14,'red')


#value can't chnage 
@dataclass(frozen=True)
class Point:
    x:int
    y:int

point=Point(3,4)

print(point.x)


@dataclass
class Person1:
    name:str
    age:int


@dataclass
class Employee(Person1):
    employee_id:str
    department:str

per=Person1('Krish',31)
employ=Employee("Kri",31,'123','AI')

@dataclass
class Address:
    steet:str
    city:str
    zip_code:str

@dataclass
class Person2:
    name:str
    age:str
    address: Address


address=Address('123 mains street','Sikta','12345')
person=Person2("Krish",31,address)

print(person.address)
