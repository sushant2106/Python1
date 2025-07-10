import pydantic
from typing import Optional
import string

class User(pydantic.BaseModel):
    username:str
    password:str
    age:int
    score:float
    email:Optional[str]
    phone_number:Optional[str]


    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_phone_or_mail(cls,values):
        if "email" in values or "phone_number" in values:
            return values
        else:
            raise ValueError("Need either email or phoneNumber")
    
    @pydantic.validator("username")
    @classmethod
    def username_valid(cls,value):
        if any(p in value for p in string.punctuation):
            raise ValueError("Username must not include punchuation")
        else:
            return value


    @pydantic.validator("password")
    @classmethod
    def password_valid(cls,value):
        if len(value)<8:
            raise ValueError("Password must be at least 8 characters long")
        
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):
                        return value
    
        
        raise  ValueError("Password needs at least one punctuation symbol,digit,upper and lower case")


    @pydantic.validator("age","score")
    @classmethod
    def number_valid(cls,value):
        if value>=0:
            return value
        else:
            raise ValueError("Number must be positive")
     



user1=User(username="Sachin1",password="12345678@_Bc",age=20,score=0,email="sam@gmail.com",phone_number="")
print(user1)

