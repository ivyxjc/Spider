import requests
from io import StringIO
import json


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

r=requests.get('https://github.com/timeline.json')
print(r.text)
print(r.encoding)

print(r.content)#二进制响应内容


r=requests.get('http://ww2.sinaimg.cn/mw600/a657ded3gw1f2nk2si1ajj20hs0ja761.jpg',stream=True)
print(r.raw)

with open('aa.jpg','wb') as f:
    f.write(r.content)


