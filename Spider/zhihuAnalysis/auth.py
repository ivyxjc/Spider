from http import cookiejar
import requests
import re
from zhihuAnalysis.LogAndError import *
import random
import sys
import platform
import os
import termcolor
from configparser import ConfigParser
import json



requests=requests.Session()
requests.cookies=cookiejar.LWPCookieJar('cookies')

"""
@:return 返回为xsrf字符串，若未找到则为None
"""

def get_xsrf():
    headers={
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Referer': 'http://www.zhihu.com/',
        'Connection':'keep-alive',
    }

    url='http://www.zhihu.com/'
    r=requests.get(url,headers=headers)
    if int(r.status_code)!=200:
        raise NetworkError("验证码请求失败")
    else:
        print(r.status_code)

    result = re.compile(r"\<input\stype=\"hidden\"\sname=\"_xsrf\"\svalue=\"(\S+)\"", re.DOTALL).findall(r.text)

    if len(result)<1:
        Logging.error("提取xsrf失败")
        return None
    print(result)
    return result

def get_captcha_code():
    headers={
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection':'keep-alive',
    }

    url = "http://www.zhihu.com/captcha.gif"
    # r = requests.get(url, params={"r": random.random()} )
    r = requests.get(url,headers=headers,params={"r": random.random()})
    if(int(r.status_code)!=200):
        raise NetworkError("验证码请求失败")
    else:
        print(r.status_code)
        print('get_captcha_code()')

    image_name="verify."+r.headers['content-type'].split('/')[-1]

    with open(image_name,'wb') as f:
        f.write(r.content)

    Logging.info("正在调用外部程序渲染验证码...")

    #todo 增加其他平台支持
    if platform.system() == "Windows":
        os.system("%s" % image_name )
    captcha_code=input(termcolor.colored("请输入验证码：","blue"))

    return captcha_code

def read_account_config(config_file="config.ini"):
    cf=ConfigParser()
    if os.path.exists(config_file) and os.path.isfile(config_file):
        Logging.info("正在加载配置文件...")
        cf.read(config_file)

        email=cf.get("info","email")
        password=cf.get("info","password")

        if email=="" or password=="":
            Logging.warn("config中账号信息无效")
            return (None,None)
        else:
            return (email,password)
    else:
        Logging.error("配置文件加载失败！")
        return (None,None)



def build_form(account,password):
    if re.match(r"^1\d{10}$", account):
        account_type = "phone_num"
    elif re.match(r"^\S+\@\S+\.\S+$", account):
        account_type = "email"
    else:
        raise AccountError("账号类型错误，请检查账号")

    form={"password":password,"remember_me":True}
    form['email']='ivyxjc1994@hotmail.com'
    form['_xsrf']=get_xsrf()[0]
    form['captcha']=get_captcha_code()
    return form

    """
    form=
    {
        xsrf:
        captcha:
        account:
        password:
        email:}
    """

def upload_form(form):
    if 'email' in form:
        url="http://www.zhihu.com/login/email"
    elif 'phone_num' in form:
        url="http://www.zhihu.com/login/phone_num"
    else:
        raise ValueError("账号类型错误")

    headers={
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'*/*',
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.zhihu.com/',
        'Content-Length': '125',
        'Connection':'keep-alive',
    }

    print(form)
    r=requests.post(url,data=form,headers=headers)
    if int(r.status_code)!=200:
        raise NetworkError("表单上传失败")

    print
    if r.headers['content-type'].lower()=="application/json":
        print(r.text)
        try:
            result=json.loads(r.text)
        except Exception as e:
            Logging.error("JSON解析失败！")
            Logging.debug(e)
            Logging.debug(r.content)
            print(r.content)
            result={
                "r":2
            }

        if result['r']==0:
            Logging.success("登录成功")
            return {"result":True}
        elif result['r']==1:
            Logging.success("登录失败")
            return{
                "error":{
                    "errcode":int(result['errcode']),
                    "message":result['msg'],
                    'data':result['data']
                }
            }
        else:
            Logging.warn("表单上传出现未知错误:"+str(result))
            return {
                "error":{
                    "code":-1,
                    "message":"unknow error"
                }
            }
    else:
        Logging.warn("无法解析服务器的响应内容:"+r.text)
        return {
            "error":{
                "code":-2,
                "message":"parse error"
            }
        }






def login(account=None,password=None):
    if islogin()==True:
        Logging.info("已经登录")
        return

    if account==None:
        (account,password)=read_account_config()
    if account==None:
        account=input("请输入登录账号:")
        password=input("请输入密码:")

    form_data=build_form(account,password)

    """
        result:
            {"result": True}
            {"error": {"code": 19855555, "message": "unknow.", "data": "data" } }
            {"error": {"code": -1, "message": u"unknow error"} }
    """

    result=upload_form(form_data)

    if "error" in result:
        if result["error"]["errcode"]==1991829:
            Logging.error("验证码输入错误，请准备重新输入")
            return login()
        else:
            Logging.warn("unknow error")
            return False
    elif "result" in result and result['result']==True:
        # 登录成功
        Logging.success(u"登录成功！" )
        requests.cookies.save()
        return True



def islogin():
    url="http://www.zhihu.com/?next=/settings/profile"
    r=requests.get(url,allow_redirects=False)
    status_code=int(r.status_code)

    if status_code==301 or status_code==302:
        return False
    elif status_code==200:
        return True
    else:
        Logging.warn("网络故障")
        return None


if __name__ == "__main__":
    # login(account="xxxx@email.com", password="xxxxx")
    # login()
    login()