import random
import base64
# from douban.settings import

class ProxyMiddleware(object):
    def __init__(self):
        self.flag=0

    def process_request(self, request, spider):
        self.flag+=1
        if(self.flag%2==0):
            request.meta['proxy'] = ''
            # request.meta['dont_redirect']=True
        else:
            request.meta['proxy'] = 'http://127.0.0.1:8080'
            # request.meta['dont_redirect']=True