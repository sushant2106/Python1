from threading import *
import time

def job1():
    print('job1 execution....')
    print(current_thread().name,'is daemon:',current_thread().daemon)
    ct=Thread(target=job2,name='ChildThread2')
    print('t is daemon:',ct.daemon)
    ct.start()

def job2():
    print('job2 excution..')


t=Thread(target=job1,name='Child Thread')
t.daemon=True
time.sleep(10)
t.start()




if __name__== '__main__':
    pass