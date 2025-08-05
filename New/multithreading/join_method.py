from threading import *
import time
# def display(number):
#     x=[x for x in number if x%2==0]
#     print('threadname:',x,current_thread().name,active_count())



# t1=Thread(target=display,args=([1,2,3,4,5],))
# t1.start()

def display():
    for i in range(10):
        print('Seetha Thread')
        time.sleep(2)


t1=Thread(target=display)
t1.start()
#t1.join() #main thread will entered into waiting state 
#t1 thread will complete first

#withing 10 sec if its not complete I will run my Ram thread then
#use this t1.join(10)

t1.join(10)
print(t1.ident)

for i in range(10):
    print('Ram Thread')