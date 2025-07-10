def apply_fun(add,x,y):
    return add(x,y)

def add(x,y):
    return x+y

print(apply_fun(add,2,3))

#assigned to variable
def greet():
    return "Hello.."

my_fun=greet

print(my_fun())



# def create_adder(x):
#     def adder(y):
#         return x*y
    
#     return adder
# add_15=create_adder(15)
# print(add_15(10))

def smaple_deco(func):
    def wrapper(*args,**kwargs):
        print(func(*args,**kwargs))
    return wrapper

@smaple_deco
def bold_div(html):
    return html

bold_div("abcd")

    
