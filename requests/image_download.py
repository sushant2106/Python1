import requests
from PIL import Image
from io import BytesIO


r=requests.get("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&psig=AOvVaw3bPDt2KsfnNhTXbgEL_kUQ&ust=1755751605988000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOCsieTJmI8DFQAAAAAdAAAAABAK")

print(r.status_code)
print(r.headers['Content-Type'])
# with open("img.jp","wb") as fp:
#     i=Image.open(BytesIO(r.content))
#     i.save(fp)
# i = Image.open(BytesIO(r.content))
# fp=open("img.jp","wb")
# i.save(fp)
# fp.close()