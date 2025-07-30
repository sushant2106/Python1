
# import os
# # print(os.listdir())


# try:
#     x=int(input("Enter the first:"))
#     y=int(input("Enter the second no:"))
#     print(x/y)

# # except BaseException:
# #     print("Come to catch ")
# # finally:
# #     print("I am finally..")

# except ArithmeticError: #parent to child 
#     print('Arithmetic erro')  #work from top to bottom
# except ZeroDivisionError as msg:
#     print(msg)

# except ValueError as msg:
#     print(msg)

# except FileNotFoundError as msg:
#     print(msg)

# #always should be last
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)

# #Default except Block

# except:
#     print("Default value ")

# finally: 
#     print("for Cleanup code")


# try:
#     a=2
#     b=0
#     X=1/a
#     os._exit(0) #python virtual machine get shut down
#     #now finally block not run


# except ValueError:
#     print('valueerror')

# finally:
#     print("PEHLE HUM")


try:
    print("outer try block")
    try:
        print("Inner try block")
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("Outer finally block")
    






if __name__ == '__main__':
    pass