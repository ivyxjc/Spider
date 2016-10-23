import requests
import json


headers={
    'apikey':'91f6d86a5fac8b8fe16970b3af6d2124'
}
url="http://apis.baidu.com/apistore/weatherservice/recentweathers?cityname=北京&cityid=101010100"
# url="http://apis.baidu.com/heweather/weather/free?city=beijing"
url='http://apis.baidu.com/apistore/weatherservice/citylist?cityname=盐都'
res=requests.get(url,headers=headers)
print(res.text)
