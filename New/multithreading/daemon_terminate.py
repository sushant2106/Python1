from threading import *
import time
def job():
    for i in range(10):
        print('LAzy thrread')
        time.sleep(3)




t=Thread(target=job)
t.daemon=True
t.start()

time.sleep(10)
print('End of Main Thread..')

#child thread is still executing despite Main thread end 
#beacuse child thread is also Non-Daemon 


#BZ CHILD thread jo True kr diya hai
#Now child thread become Daemon thread 

