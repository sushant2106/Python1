

def outer_fun():
    message='Hii'

    def inner_fun():
        print(message)
    return inner_fun


my_fun=outer_fun()
my_fun()