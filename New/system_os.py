import os

# print(os.system("dir *.py"))

# os.system("demo.py")

# os.system("notepad")


#How to get info of content file

import os
from  datetime import datetime 
stats=os.stat("abc.txt")
print("File size in bytes",stats.st_size)
print("File last Accessed time",datetime.fromtimestamp(stats.st_atime))
print("File last Modified Time",datetime.fromtimestamp(stats.st_mtime)) 
print("File last Mod")
