from  threading import *
import time 


def display():
    print(current_thread().name,'started....')
    time.sleep(3)
    print(current_thread().name,'ended....')



print('The number of active threads:',active_count())

t1=Thread(target=display,name='Child Thread-1')
t2=Thread(target=display,name='Child Thread-2')
t3=Thread(target=display,name='Child Thread 3')

t1.start()
t2.start()
t3.start()

print(t1.name,'is alive',t1.is_alive())
print(t2.name,'is alive',t2.is_alive())
print(t3.name,'is alive',t3.is_alive())


time.sleep(10)



print(t1.name,'is alive',t1.is_alive())
print(t2.name,'is alive',t2.is_alive())
print(t3.name,'is alive',t3.is_alive())