import time

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
doubles(numbers)
squares(numbers)
endtime=time.time()

print('The total time taken:',endtime-begintime)