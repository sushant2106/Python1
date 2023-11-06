
def outer_fun(msg):
    message=msg

    def inner_fun():
        print(message)
    
    return inner_fun



hi_func=outer_fun('Hi')
bye_func=outer_fun('Bye')


hi_func()