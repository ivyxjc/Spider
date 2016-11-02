import requests
import re
import socket

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()

    return ipaddr

class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://www.ip.cn/")
        except:
            try:
                myip = self.visit("http://dir.twseo.org/ip-check.php")
            except:
                try:
                    myip = self.visit("http://ip111.cn/")
                    # if you want to add more,use the format "except try"
                    # make sure the most useful link be the first
                except:
                    print("Fail to get the Network ip.")
                    print("Get the LAN ip.")
                    myip = get_lan_ip()
        return myip

    def visit(self,url):
        opener = requests.get(url)
        # print(opener.url)
        if url == opener.url:
            str = opener.text
            print("IP information from",url)
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

def get_network_ip():
    getmyip = Getmyip()
    localip = getmyip.getip()
    print(localip)
    return localip

get_network_ip()
# opener = requests.get("http://www.ip.cn/",timeout=20)
# str = opener.text
# print(str)
