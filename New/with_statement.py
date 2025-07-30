# with open('with_abc.txt','w') as f:
#     f.write('Durga Ji\n')
#     f.write('Ram ji\n')
#     print("is file close",f.closed)

# print('is file closed ',f.closed)



# with open('with_abc.txt','r') as f:
#     print(f.tell())
#     print(f.read(4))
#     print(f.tell())
#     print()



#seek() move cursor for specific location 
#f.seek(offset,fromwhere)

# 0 from beginning of file(dafault file)

data='All student are Nice'
f=open('abc.txt','w')
f.write(data)
with  open('abc.txt','r+') as f:
    text=f.read()
    print(text)
    print('current cursor pos:',f.tell())
    f.seek(16) #mocve the cursor to specific location
    print('now current cursor pos:',f.tell())
    f.write("GEMS!!")
    f.seek(0)
    text2=f.read()
    print(text2)


#how to check weather file exist or not
#file information 

import os,sys

fname=input('Enter the filename:')

if os.path.isfile(fname):
    print('file Exists:',fname)
    f=open(fname,'r')
    print('The current file')
    data=f.read()
    print(data)
    f.close()

else:
    print('file not exist',fname)
    sys.exit(0)


# print('The current file')
# data=f.read()
# print(data)
