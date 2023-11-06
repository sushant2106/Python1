
def logger(msg):

    # def log_message(kk):
    #     print('log:',msg)
    #     print(kk)
    def log_message():
        print('log:',msg)

    return log_message


log_hi=logger('Hii..')

# log_hi("Hello")

log_hi()
