
def square(x):
    return x*x

# f=square

# print(square)
# print(f(5))


def my_map(fun,arg_list):
    res=[]
    for i in arg_list:
        res.append(fun(i))

    return res


squarees=my_map(square,[1,2,3,4,5])

print(squarees)

# print(list(map(square,[1,2])))