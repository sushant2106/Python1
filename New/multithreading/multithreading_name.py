from threading import *

print(current_thread().name)

# current_thread().setName('Ram ji')
current_thread().name='Ram ji'

print(current_thread().name)

