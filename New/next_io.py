l=(x*x for x in range(100000000000)) #generator
#in no object will store in memory

#its generator not comprehension
print(next(l))
print(next(l))
print(next(l))

# l2=[x*x for x in range(10000000000000)]
#object will stored in memory


#generator doesn't store in memory


def decor2(func):
    def inner(name):
        print("decoraring 2 executing..")
        func(name)
    return inner

def decor1(func):
    def inner(name):
        print("decoraring 1 executing..")
        func(name)
    return inner


def decor(func):
    def inner(name):
        if name=='Sunny':
            print('Hello inner')
        else:
            print('I am else fun')
            func(name)
    return inner


@decor2
@decor1
def wish(name):
    print(name)

wish("Durga")




def double_decor(func):
    def inner():
        print('I am double')
        x=func()
        return 2*x
    return inner

def square_decor(func):
    def inner():
        print('I am square')
        x=func()
        return x*x
    return inner


@double_decor
@square_decor
def num():
    # print("I am last")
    return 10

print(num())




