
def square(x):
    return x*x

# f=square(5)
# f=square  # we can treat function f as variable
# print(square)
# print(f(5))

def my_app(fun,arg_list):
    result=[]
    for i in arg_list:
        result.append(fun(i))
    return result

squares=my_app(square,[1,2,3,4,5])
print(squares)

#return the function


def logger(msg):
    def log_messgae():
        print('Log:',msg)
    return log_messgae

log_hi=logger('Hi..!')
log_hi()