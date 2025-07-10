class User:
    total_user=0
    def __init__(self,name):
        self.name=name
        self.total_user+=2
        User.total_user+=1
    
    @staticmethod
    def salutation(user_name):
        return user_name
    @classmethod
    def display(cls):
        print("Total USer",cls.total_user)
    


user=User("ALice")
user2 = User("Bob")

User.display()

User.total_user=5

print(user2.total_user)

