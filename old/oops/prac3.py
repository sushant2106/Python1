
# my_set={1,2,3}

# print(my_set)
# my_tuple=(4,5,6)

# new_tuple=my_tuple+(9,)

# print(new_tuple)

# my_set.add(11)

# print(my_set)

#Functions can be passed as arguments to other functions
#Higher order function
# def supply(add,x,y):
#     return add(x,y)

# def  add(x,y):
#     return x*y

# print(supply(add,2,4))


# def create_mult(fact):
#     def mult(x):
#         return x*fact
#     return mult

# double=create_mult(2)
# print(double(5))


#first class fucntion

def cutom_iterator(start,end):
    current=start
    while current<end:
        yield current
        current+=2

itr=cutom_iterator(1,10)
for num in itr:
    print(num)
