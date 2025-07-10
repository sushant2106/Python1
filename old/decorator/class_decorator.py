

def decorator_fun(orignal_function):
    def wrapper_fun(*args,**kwargs):
        print('wrapper executed this before {}'.format(orignal_function.__name__))
        return orignal_function(*args,**kwargs)
    
    return wrapper_fun


class decorator_class(object):
    def __init__(self,orignal_function):
        self.orignal_function=orignal_function

    def __call__(self, *args,**kwargs):
        print('wrapper executed this before {}'.format(self.orignal_function.__name__))
        return self.orignal_function(*args,**kwargs)





@decorator_class
def display():
    print('display function ran')


@decorator_class
def display_info(name,age):
    print('display_info ran with ({},{})'.format(name,age))



display_info('Ram',25)
display()