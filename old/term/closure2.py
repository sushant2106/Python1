def outer_fun(msg):
    message=msg

    def inner_func():
        print(message)

    return inner_func




hi_func=outer_fun('Hi')
hello_fun=outer_fun('Hello')


hi_func()

hi_func()