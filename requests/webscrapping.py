import requests

# DatAcOLLECTION=

links=['https://www.codewithharry.com/blog','https://www.codewithharry.com/videos','https://www.codewithharry.com/tutorial/overview/cplusplus-overview']

for link in links:
    r=requests.get(link)
    with open(f"HTML/{link.split('/')[-1]}.html",'w',encoding="utf-8") as f:
        f.write(r.text)