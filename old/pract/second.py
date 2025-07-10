import httpx

r=httpx.get('http://api.github.com/user',auth=('user','pass'))


print(r.status_code)

print(r.content)


print(r.encoding)