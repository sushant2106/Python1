import os

os.environ['key']="2345"

env=os.getenv('key')
print(env,type(env))

env1=os.environ.get("key")



print(os.getenv('Path'))