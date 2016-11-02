import requests
import json


token={"access_token":"2.007eRNvC25ZpvC9f70a9c354_EF9UB",
"remind_in":"157679999",
"expires_in":157679999,
"uid":"2677682934"}

access_token="2.007eRNvC25ZpvC9f70a9c354_EF9UB"


url="https://api.weibo.com/2/statuses/public_timeline.json?access_token="+access_token
print(url)

r=requests.get(url)

if(r.status_code==200):
    print(r.text)
else:
    print(r.status_code)

