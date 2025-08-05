import time
# class Test:
#     def __init__(self):
#         print('Obhect Intitalization')
    
#     def __del__(self):
#         print('Fulfilling lastwish and performing clean up activities')



# t1=Test()
# t1=None

# time.sleep(5)
# print('End of Application')


# class Test2:
#     def __init__(self):
#         print('Obhect Intitalization')
    
#     def __del__(self):
#         print('Destructor Executon...')

    



# t1=Test2()
# del t1
# time.sleep(5)
# print('End')

# ###############
# print()
# print('I am 3...')
# print()
# class Test3:
#     def __init__(self):
#         print('Object Intitalization')
    
#     def __del__(self):
#         print('Fulfilling lastwish and performing clean up activities')



# t1=Test3()
# print('T1:',t1)
# t2=t1 
# t3=t2
# del t1
# print('Object not yet destroyed after deleting t1')

# print('T2:',t2)
# time.sleep(5)
# del t2
# time.sleep(10)
# print('Object not yet destroyed after deleting t2')
# print('I am trying to delete t3 also ...')
# del t3


# print()


class Test4:
    def __init__(self):
        print('Constructor Execution...')
    
    def __del__(self):
        print('Destructor Execution....')


l1=[Test4(),Test4(),Test4()]

time.sleep(8)
del l1
time.sleep(7)
print('End of Application..')


