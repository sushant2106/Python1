# from typing import NewType,TypedDict
from typing import NewType
from dataclasses import dataclass
import random
import os 

name : str ="corey"
age : int=38
RGB =NewType("RGB",tuple[int,int,int])
HSL=NewType("HSL",tuple[int,int,int])

# class User(TypedDict):
#     first_name:str
#     last_name:str
#     age: int | None
#     fav_color : RGB | None


# type RGB= tuple[int,int,int]
#type User=dict[str,str |int | RGB |None] #type alias value
# type HSL=tuple[int,int,int]

@dataclass
class User:
    first_name:str
    last_name:str
    email: str
    age: int | None = None
    fav_color : RGB | None =None




# def create_user(first_name : str,last_name:str,age:int | None =None)-> dict[str,str | int | None]:
def create_user(first_name : str,last_name:str,age:int | None =None,fav_color: RGB |None=None)-> User:
    email=f"{first_name.lower()}_{last_name.lower()}@example.com"
     
    # str_age=str(age)
    # return {
    #     "first_name":first_name,
    #     "last_name":email,
    #     "age":age,
    #     "fav_color":fav_color,
    # }
    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color,
    )
    


# user1=create_user('Corey','Schafer',age=38,fav_color=(109,12,134))
# user2=create_user("John","Doe",fav_color=(206,10,48))



def random_choice(items: list[User]) -> User:
    return random.choice(items)



user1=create_user('Corey','Schafer',age=38,fav_color=RGB((109,12,134)))
user2=create_user("John","Doe",fav_color=RGB((206,10,48)))

# print(user1)
# print(user2)

users=[user1,user2]
random_user=random_choice(users)
print(random_user)

emails=[user.email for user in users]
random_email=random_choice(emails)

print(random_email)



print(os.getcwd())