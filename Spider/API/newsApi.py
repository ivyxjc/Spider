
import requests


url = 'http://apis.baidu.com/showapi_open_bus/channel_news/search_news'
args={'page':2}
res=requests.get(url,headers={'apikey':'91f6d86a5fac8b8fe16970b3af6d2124'},params=args)
print(res.text)