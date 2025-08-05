from threading import * 

# def display():
#     print('THis code executed by thread',current_thread().name())



def display():
    ''' this display is executed by child thread '''
    for i in range(10):
        # print('Child Thread',current_thread().name)
        print('Child THread..')
t=Thread(target=display)
#main thread created child thread object  but didn't started child thread 

t.start() #this line main thread start  the child thread 

# print(current_thread().name)
for i in range(10):
    print('Main Thread')



