# import threading
# print('Current Executuing Thread:',threading.current_thread())


#the ways of creating thread in Python 


from threading import *

def display():
    print('(display-fucntion) executed by thread:',current_thread().name) #earlier we had getName()


#print('This code executed by thread:',current_thread().name)
t=Thread(target=display) #MaIN THREAD create  child thread object

print('This code executed by thread:',current_thread().name)


#main thread create child thread object
#child thread object is responsible to execute dislay method(job) 

t.start() #Mainthread starts child thread 

#jaise hi t.start() it will create child thread and 
#start executing display function
