def outerfun():
    message='Hi'
    def inner_fun():
        print(message)
    return inner_fun()

print(outerfun())






# def logger(msg):
#     def log_messgae():
#         print('Log:',msg)
#     return log_messgae

# log_hi=logger('Hi..!')
# log_hi()