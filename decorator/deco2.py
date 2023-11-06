
def decorator_fun(orignal_function):
    def wrapper_fun():
        return orignal_function()
    
    return wrapper_fun




def display():
    print('display function ran')


decorated_display=decorator_fun(display)

decorated_display()