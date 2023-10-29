# import yaml

# data={
#     "name":"Nike",
#     "age":25,
#     "languages":["python","c","Java"],
#     "Address": {
#         "city":"banglore",
#         "Country":"Bharat"
#     }

# }

# with open("somefile.yaml","w") as f:
#     yaml.dump(data,f,default_flow_style=False)

import os 
  
# # Path 
# path = "/home / User / Desktop / file.txt"
  
# start = "/home / User"

# relative_path = os.path.relpath(path, start) 
  
# print(relative_path) 
# print(os.path.curdir)
print(os.path.realpath(os.path.curdir))