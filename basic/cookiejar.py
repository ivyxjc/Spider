from http import cookiejar
import requests

# cookie=cookiejar.CookieJar()

# requests=requests.Session()
# requests.cookies=cookiejar.LWPCookieJar()
r=requests.get('http://www.baidu.com')
print(r.cookies['example_cookie_name'])