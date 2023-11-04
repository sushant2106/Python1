import os
from datetime import datetime
# print(dir(os))

#print(os.getcwd())

os.chdir('/Users/Sushant Gupta/Desktop/')
# print(os.getcwd())

#print(os.listdir()) # by default it will give you current directory

# os.mkdir("os-demo") mkdir will just create directory

#but when you want to create sub directory (folder inside folder)

# os.makedirs('os-demo/sub-dir-1')

# os.mkdir('os-demo-2')

######################################

#to delete
# os.rmdir('os-demo-2')

# os.removedirs('os-demo/sub-dir-1')
# os.makedirs('os-demo/sub-dir-2')
# os.removedirs('os-demo/sub-dir-1')

# os.rename('bracnh.txt','git_branch.txt')

# mod_time=os.stat('git_branch.txt').st_mtime

# print(datetime.fromtimestamp(mod_time))

# print(datetime.now())

# for dirpath,dirnames,filenames in os.walk('/Users/Sushant Gupta/Desktop/'):
#     print('Current Path:',dirpath)
#     print('DirectoriesName:',dirnames)
#     print('Files',filenames)
    

# print(os.environ.get('HOME'))

file_path='/Users/Sushant'

# new_file_path=os.path.join(os.getcwd(),'test.txt')
# print(new_file_path)

get_base_name=os.path.basename('/tmp/test.txt')
print(get_base_name)

get_dir_name=os.path.dirname('/tmp/test.txt')
print(get_dir_name)


want_both=os.path.split('/tmp/test.txt')
print(want_both)

print(os.path.exists('/tmp/test.txt')) #os.path.isdir/isfile

file_path_extension=os.path.splitext('/tmp/test.txt')
print(file_path_extension)


# print(dir(os.path))

# print(os.path.relpath(os.getcwd()))

