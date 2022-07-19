from lxml import etree
import os

import requests

"""

这个文件是用来更新github的host地址的

"""

header = {
    'Host': 'ipaddress.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Referer': 'https://www.ipaddress.com/',
}

res = requests.get(url='https://ipaddress.com/website/github.com', headers=header)
res = res.text
# print(res)

html = res
tree = etree.HTML(html)
ip = tree.xpath("//*[@class='comma-separated']/li/text()")[0]
print(ip)
fileName = r'C:\Windows\System32\drivers\etc\hosts'
content_txt = ip + ' ' + 'github.com'

with open(fileName, 'w')as file:
    file.write(content_txt)

os.system("ipconfig /flushdns")
