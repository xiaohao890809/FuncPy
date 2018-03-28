import requests
import re

i = 0

res = requests.get('https://www.imooc.com/search/course?words=python').text
urllist = re.findall(r'//.*?\.jpg',res)

# 将图片保存到本地
for url in urllist:
    f = open(str(i)+'.jpg','wb')
    req = requests.get('http:'+url).content
    f.write(req)
    f.close()
    i += 1



