class Student:
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add

    def check_valid_age(self):
        try:
            if self.age >0:
                print("Good ")
            else:
                print("Its okay")
        
        except  Exception as e:
            print(f'Error in the file {e}')

    def add_num(self):
        self.add=self.add+5
        print(self.add)


class Stud(Student):
    def __init__(self, name, age, add):
        super().__init__(name, age, add)
        print('Calling parent function')


if __name__ == '__main__':
    # name=input("Enter the name:")
    # age=int(input("Enter the age:"))
    # obj=Student(name=name,age=age,add=3)
    # obj.check_valid_age()
    # obj.add_num()

    # obj2=Student('Ram',24,6)
    # obj2.add_num()
    # obj.add_num()

    obj=Stud('ram',21,4)
    obj.check_valid_age()



