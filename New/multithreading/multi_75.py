from threading import *

def test():
    print('Child Thread..',current_thread().ident)

def test2():
    print('child Thread2:',current_thread().ident)


t=Thread(target=test)
#to set threadname

t.name='pawan kalyan thread'
t.start()


# or another way tos set thread name

t2=Thread(target=test2,name='Anusilan Samiti..')

t2.start()





print('Threaad name:',t.name)
print('Raur thread name:',t2.name)
print('Mian thread Identification no:',current_thread().ident)
print('Child Thread Identification Number:',t.ident)

print('Active count thread:',active_count()) #threading.active_count()
t.join()
t2.join()


#active_count() will tell number of current_executing thread
#How manythreads are available 








if __name__== '__main__':
    pass