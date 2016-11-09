from scrapy.cmdline import execute
import time


t1=time.time()
execute(['scrapy','crawl','douban'])
print(time.time()-t1)
