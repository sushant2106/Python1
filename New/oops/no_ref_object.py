# import sys
# class Test:
#     pass

# t1=Test()
# t2=t1
# t3=t1
# t4=t1


# print(sys.getrefcount(t1))

import time

class Test:
    
    def __del__(self):
        print('Destructor Execution...')

t1=Test()
t2=Test()
# del t1
time.sleep(5)