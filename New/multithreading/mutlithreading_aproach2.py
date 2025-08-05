#create thread using class 

from threading import *
class MyThread(Thread):
    ''' we are overriding job method '''
    def run(self): #this become job of thread
        for i in range(10):
            print('Child Thread-1')


t=MyThread()
t.start()

for i in range(10):
    print('Main Thread-1')


if __name__ == '__main__':
    pass


