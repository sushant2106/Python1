

def decorator_fun(orignal_function):
    def wrapper_fun(*args,**kwargs):
        print('wrapper executed this before {}'.format(orignal_function.__name__))
        return orignal_function(*args,**kwargs)
    
    return wrapper_fun



@decorator_fun
def display():
    print('display function ran')


@decorator_fun
def display_info(name,age):
    print('display_info ran with ({},{})'.format(name,age))



display_info('Ram',25)
display()