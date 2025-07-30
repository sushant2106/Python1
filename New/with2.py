# f=open('wrth_2.txt','w')
# f.write('abcd\n')
# f.write('efg')

import os


# fname=input('ENter the file name:')
# if os.path.isfile(fname):
with open('wrth_2.txt','r') as f:
    # data=f.read()
    # print(data)
    list=f.readlines()
    print(len(list))
    sum=0
    for x in list:

        sum+=len(x)
    print(sum)





