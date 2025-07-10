# class  School:
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.__year=2024
    
#     def disp(self):
#         print(self.__year)
        


# class small(School):
#     def __init__(self,name,age,name2):
#         super().__init__(name,age)
#         self.name=name2

#     def display(self):
#         print(f'{self.name}')

        



# obj=School("Ram",21)
# obj.disp()

# obj=small("Ram",21,'shyam')
# obj.display()

class USers:
    
    def __init__(self,name,password,role,user):
        self.name=name
        self.password=password
        self.role=role
        self.user=user

    def add_user(self):
       x={"name":self.name,"password":self.password,"role":self.role}
       self.user.append(x)
      

    def update_user_password(self,name,new_password):
        for x in  self.user:
            if x["name"]==name:
                self.password=new_password
                return
        
        print("Not found...")

    def delete_user(self,name):
        for x in self.user:
            if x["name"]==name:
                self.user.remove(x)
                return
        print("User not found")
        
        





obj=USers("ram","123","dev",user=[])

obj.add_user()
# obj.display()
obj.update_user_password("ram","345")
obj.delete_user("ram")


