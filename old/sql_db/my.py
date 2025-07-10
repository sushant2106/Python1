
# my_list=[1,2,"kalyan",True]

# my_list.append(8)

# print(my_list)

# my_list[0]=10

# print(my_list)

# my_tuple=(3,1,2)
# print(my_tuple)

# users=[]

# def add(name,password):
#     user={"name":name,"pasw":password}
#     users.append(user)


def fun(start,end):
    current=start

    while start<=end:
        yield current
        current+=2
        start+=1
        


ite=fun(1,5)
print(ite)

for i in ite:
    print(i)


# for i in fun(1,10):
#     print(i)
