# try:
#     print("try")
#     # print(10/0)
#     print(10/2)

# except:
#     print("except")
# else:
#     print("else")

# finally:
#     print("finally")



#try without except or finally is invalid

# try:
#     print("test")

# finally:
#     print('lets')

# '
# invlid'
# try:
#     print("try")

# else:
#     pass


try:
    print('Hello')

finally:
    print('I am finally..')

# except:
#     print('I am except')


class TooYoungExce(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg 
    
age=int(input("Enter the age:"))
if age>60:
    raise TooOldException("Plz wait for some time")
elif age<18:
    raise TooOldException("Can't do it noe")

else:
    print("Thanks for registration..")









if __name__=='__main__':
    pass