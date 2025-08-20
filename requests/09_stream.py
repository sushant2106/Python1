import requests
import time
url='https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-713ar.exe'

r=requests.get(url,stream=True)
totalBytesExpected=int(r.headers['Content-Length'])
start=time.time()
# print
if r.status_code == 200:
    with open("winrar.exe",'wb') as fp:
        for chunk in r.iter_content(chunk_size=128):
            print(f'Show me time:{time.time()}')
            fp.write(chunk)


else:
    print(r.status_code)

print(f'Show me time:{time.time()-start}')
