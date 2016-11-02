import requests
import json

url='https://api.douban.com/v2/book/1220562'
url='https://api.douban.com/v2/movie/subject/1764796'
url="https://api.douban.com/v2/movie/search?q={魔兽}"

# in_theaters_url="https://api.douban.com/v2/movie/in_theaters"
in_theaters_url="https://api.douban.com/v2/movie/subject/24827387"
movie_info_url="https://api.douban.com/v2/movie/subject/22939161"
r=requests.get(in_theaters_url)


if(r.status_code==200):
    print(r.text)
else:
    print(r.status_code)



