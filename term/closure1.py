
def outer_fun():
    message='Hi..'

    def inner_func():
        print(message)
        # return 2

    # return inner_func()
    return inner_func


# print(outer_fun())

# outer_fun()

my_fun=outer_fun()

# print(my_fun.__name__)

my_fun()