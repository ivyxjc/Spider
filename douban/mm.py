from douban.get_sitemap_xml import SiteMap
import sys
import os
import gzip
import urllib
import re
# sys.stdout = open("text\\log.txt", "a")


# s=SiteMap()
# s.create_multiple_thread(0,3783,10)


# t= gzip.open("sitemap\\sitemap0.gz",'rb')
# with open("aa",'wb')as f:
#     f.write(t.read())
# t.close()

class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://1111.ip138.com/ic.asp")
        except:
            try:
                myip = self.visit("http://ip.chinaz.com/")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                    # if you want to add more,use the format "except try"
                    # make sure the most useful link be the first
                except:
                    print("Fail to get the Network ip.")
                    print("Get the LAN ip.")
                    # myip = get_lan_ip()
        return myip
    def visit(self,url):
        opener = urllib.urlopen(url,timeout=20)
        if url == opener.geturl():
            str = opener.read()
            print("IP information from",url)
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

def get_network_ip():
    getmyip = Getmyip()
    localip = getmyip.getip()
    print(localip)
    return localip

get_network_ip()