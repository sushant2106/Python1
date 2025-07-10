# x=10
# y=3
# z=x**y
# print(z)

# # and or

# if x!=y:
#     print("I am")

# if not(x>y):
#     print("yes")
import datetime
import math
# dt=datetime.datetime.now()
# print(dt)
# print(dt.hour)


# dt1=datetime.datetime(2014,5,16)
# print(dt1.strftime("%a"))
# print(dt1.strftime("%d-%m-%Y"))
# start=datetime.datetime.now()
# a=0
# for i in range(1000000):
#     a+=i

# end=datetime.datetime.now()
# print(end-start)

# maximum=math.ceil(10.99)#floor
# print(maximum)

# inc_by_ten=lambda attr: attr + 10
inc_by_ten=lambda attr,attr2:attr + ( attr2 + 10)

print(inc_by_ten(100,2))


# python -m venv mysaml
