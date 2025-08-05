from threading import * 

print('Main thread:',current_thread().daemon)

#once thread started we are not allow to change Daemon nature 


def job():
    print('Child Thread')


t=Thread(target=job) #main is the parnet and t is child 

print(t.daemon)

#now change the nature of daemon

t.daemon=True

print(t.daemon)

