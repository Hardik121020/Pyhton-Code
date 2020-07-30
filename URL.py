from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = ("http://py4e-data.dr-chuck.net/known_by_Fikret.html ")
html = urlopen(url ,context =ctx).read()
object_1 = BeautifulSoup(html,'html.parser')

total =0
tags = object_1('a')
for tag in tags:
    total = total + 1
print(total)
