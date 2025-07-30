#memory utilization will improved

from zipfile import *

f=ZipFile('files.zip','w',ZIP_DEFLATED)

f.write('with_abc.txt','abc.txt')
f.write('abcd.txt')

f.close()
print('zipfile is created')

#to perform unzip
f=ZipFile('files.zip','r')
name=f.namelist()
print(name)

for name in name:
    print("The content of the file")
    f1=open(name,'r')
    print(f1.read())
    print()


#Work with directories 
#os module

import os 
print(os.getcwd())

# cwd=os.mkdir('subdir')
# print('subdircreated')

#nested  HERE DIRECTORY MUST BE available 
# cwd_nested_dir=os.mkdir('subdir/video')

# cwd=os.makedirs("sub1/sub2/sub3")


#to remove a directory 
# os.rmdir('subdir/video')

# print("Task Completed..")
# os.removedirs('sub1/sub2/sub3')

# os.mkdir('subham')
# os.mkdir('subham/video')

# os.rename('subham','agarwal')

#list in cwd
# print(os.listdir(os.getcwd()))



#alterntive 
# print(os.listdir('.'))

#subdirectory current also -> walk()

import os

for dirpath,dirnames,filenames in os.walk('.'):
    print('cwd',dirpath)
    print('dIRECTORIES:',dirnames)
    print("File Nmes:",filenames)
    print()

# for dirpath,dirnames,filenames in os.walk('D:\\'):
#     print('cwd',dirpath)
#     print('dIRECTORIES:',dirnames)
#     print("File Nmes:",filenames)
#     print()


# with open('a.txt','w') as f:
#     f.write('abcdd')
  

# os.mkdir()
# os.getcwd()

