import re
import urllib.request
import urllib.parse
str1="I love 123 FishC.com"

res=re.search(r'love',str1)

res=re.search(r'love',str1)

res=re.search(r'\d\d\d',str1)

res=re.search(r'[a-zA-Z]',str1)

res=re.search(r'ab{3,10}c','aaabbbbbbbbbbc')

res=re.search(r'^FishC','FishC.com!')

res=re.search(r'(ABC)(.com)\2','ABC.com.com')

res=re.search(r'(ABC)\060','ABC0')

res=re.findall(r'[^a-z^]','FishC\.co\m^')


res=re.search(r'ABC{2,8}?','ABCCCCCC')

p=re.compile(r'(Love) (You)')
res=p.search('I Love You')
print(res.group(0))
print(res.group(1))
print(res.group(2))

print(res.start())
print(res.end())
print(res.span())

res=re.findall(r'\w','我爱你 ，大家好_No')

res=re.search(r'abc(?=.com)','abcaeabc.com')
res=re.search(r'(?<=abc).com','.com.abc.com')
print(res)

str1='<tr> \
            <td>221.179.236.252</td>\
                <td>8123</td>\
                <td>高匿名</td>\
                <td>HTTP</td>\
                <td> <a href="/free/inha/2016-03/xicangzizhiqulasashi">西藏自治区拉萨市</a></td>\
                <td>3秒</td>\
                <td>2016-03-29 11:51:45</td>\
            </tr>\
            <tr>\
                <td>118.249.192.146</td>\
                <td>9000</td>\
                <td>高匿名</td>\
                <td>HTTP</td>\
                <td><a href="/free/inha/2016-03/hunansheng">湖南省</a> <a href="/free/inha/2016-03/changshashi">长沙市</a></td>\
                <td>3秒</td>\
                <td>2016-03-29 10:51:43</td>\
            </tr>\
            <tr>\
                <td>36.46.17.183</td>\
                <td>8090</td>\
                <td>高匿名</td>\
                <td>HTTP</td>\
                <td><a href="/free/inha/2016-03/shanxisheng">陕西省</a> <a href="/free/inha/2016-03/xianshi">西安市</a></td>\
                <td>2秒</td>\
                <td>2016-03-29 09:51:43</td>\
            </tr>'
# pattern=re.compile(r'[01]\d\d|2[0-4]\d|25[0-5]')
res=re.findall("<td>([\d|.]+)</td>",str1)


for i in range(0,len(res),2):
    print(res[i]+":"+res[i+1])

str1='<a href="http://jandan.net/ooxx/page-1924#comment-3097931">48081</a></span><p><a href="http://ww1.sinaimg.cn/large/66b3de17gw1f2e0ubvyz5j21e00xcan8.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/mw600/66b3de17gw1f2e0ubvyz5j21e00xcan8.jpg" /></p>\
<div class="vote" id="vote-3097931"><span id="acv_stat_3097931"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3097931" href="javascript:acv_vote(3097931,1);">OO</a> [<span id="cos_support-3097931">7</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3097931"  href="javascript:acv_vote(3097931,0);">XX</a> [<span id="cos_unsupport-3097931">1</span>]</div>\
</div>\
                    </div>'

res=re.findall(r'<a href="([^"]+.jpg)"[\s\S]+查看原图',str1)
print(res)

ss="\u5173\u6ce8\u5979".encode('utf-8')

print(ss)
print(ss.decode())
# \\u6653\\u6653



str1="icon icon-profile-female"
print(re.match(r".*female.*",str1))
if re.match(r"female",str1):
    print(0000)
