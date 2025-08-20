import requests
from PIL import Image
from io import BytesIO

url='https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-713ar.exe'

r=requests.get(url)

if r.status_code == 200:
    with open("winrar.exe",'wb') as fp:
        fp.write(r.content)

else:
    print(r.status_code)
