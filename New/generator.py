# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'


# g=mygen()

# # print(type(g))
# # print(next(g))
# # print(next(g))

# for x in g:
#     print(x)



# # def countdown(num):
# #     print("Start Count down")
# #     while num>=0:
# #         yield num
# #         num-=1


# # for x in countdown(10):
# #     print(x)



# def fibonaci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# f=fibonaci()
# for x in f:
#     if x>100:
#         break
#     print(x)

# import cal 

# print(cal.x)
# print(cal.y)
# print(cal.add(1,2))


#group of module called package

#group of package called library 

#for every module compiled file will be store
#save it python complied file
#whenever we use compile module its store module generator 

# import cal as c
# 10 hrs if module1 modified

#imp module reload() function 

# import time
# import module1
# time.sleep(30)
# print("Programming entering into sleeping state")
# import module1
# print("this is the last time")


import time
from imp import reload
import module1
time.sleep(30)
print("Programming entering into sleeping state")
time.sleep(30)
reload(module1)
print("this is the last time")







    