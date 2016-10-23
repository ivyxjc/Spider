import requests
import re
import os
headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'DNT':'1',
    'Connection': 'keep-alive',
}

cookies={
    '_utma':'51854390.1201051542.1467626439.1467626439.1467626439.1',
    '_utmb':'51854390.2.10.1467626439',
    '_utmc':'51854390',
    '_utmt':'1',
    '_utmv':'51854390.000--|3=entry_date=20160703=1',
    '_utmz':'51854390.1467626439.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '_zap':'adb49035-c78a-4d42-b9b4-39b337e837f4',
    'a_t':'"2.0AACAbwMlAAAXAAAA0cChVwAAgG8DJQAAACDA3WMMLAoXAAAAYQJVTdHAoVcAGIs6SAUQckflNnwnRoA83B7n91fzZ8go_KD1jChjr51o6bHIO81OxQ=="',
    'cap_id':'"NzYxNTkyN    WEyMzI2NDMxZGJkMzZmZjgyZmUyYTBiMDk=|1467626424|e37a070843c52014da7739faaeba76359c722550"',
    'd_c0':'"ACDA3WMMLAqPToDYC2GbnAyjeteoXyJNvGI=|1467534729"',
    'l_cap_id':'"OGJmN2FlMzdiYjM5NDIzODg1ZDE2ZjAzOGY0Y2M1MjI=|1467626424|20db834d5c5ba67e40c6d6dae5746a9c37b25862"',
    'l_n_c':'1',
    'login':'"M2Y0ZTEyMTcwMzFkNDQ1MTg1Mzc1MWI5MmIwNTNlZGI=|1467626449|a1c9cd9b1d6558abd727a4f4838db446ef5da5b0"',
    'q_c1':'4676c4e334e941feac96a624b8fe44fa|1467534729000|1467534729000',
    'z_c0':'Mi4wQUFDQWJ3TWxBQUFBSU1EZFl3d3NDaGNBQUFCaEFsVk4wY0NoVndBWWl6cElCUkJ5Ui1VMmZDZEdnRHpjSHVmM1Z3|1467626449|1b39249f445c4a0abf044518e3f2f2eee5c2e7e3',

}

url="https://www.zhihu.com/question/37811449"

html=requests.get(url,headers=headers,cookies=cookies)

text=html.text
p=re.compile('data-original=\"(https://pic\d.zhimg.com/\w+?.\w\w\w)\"')
res=re.findall(p,text)
filenumber=1

img_headers = {
    'Host':'pic1.zhimg.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'DNT':'1',
    'Connection': 'keep-alive',
}
res=list(set(res))
print(res)
os.chdir('E:\\program\\python\\spider\\zhihuAbout\\pics')
for i in res:
    imgbytes=requests.get(i,headers=img_headers,cookies=cookies)
    filename="pic"+str(filenumber)+'.jpg'
    with open(filename,'wb') as f:
        f.write(imgbytes.content)
    filenumber+=1





