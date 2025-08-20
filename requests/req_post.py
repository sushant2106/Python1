import requests
r=requests.post("https://httpbin.org/post",data={'harry':'value'})

print(r.text)