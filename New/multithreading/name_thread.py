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

#list of all active thread info
l=enumerate()
for t in l:
    print('Active thread Name:',t.name)

print('The numbe of active thread:',active_count())
time.sleep(10)

#once the job is completed the thread become dead state .Now its no more active

print('The Number of active thread:',active_count())# 1 thread i.e main thread

for t in l:
    print('After 10s name of thread:',t.name)



if __name__ =='__main__':
    pass

