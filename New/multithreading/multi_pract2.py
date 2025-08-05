import time
from threading import *
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print('Double :',2*i)



def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)


numbers=[1,2,3,4,5,]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()


#Main thread have to wait 
t1.join()
t2.join()

endtime=time.time()

print('The total time taken:',endtime-begintime)


if __name__=='__main__':
    pass