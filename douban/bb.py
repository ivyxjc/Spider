import json

# map={}
# for i in range(0,3783):
#     map[i]=0
#
# with open("text\\sitemap_config.json","w") as f:
#     json.dump(map,f)

# map={}
# with open("text\\sitemap_config.json", 'r') as f:
#     map = json.load(f)
# print(map)
import threading
import time
import json
import random

print(random.randint(0,3783))

map={}
with open('text\\sitemap_config.json', 'r') as f:
    map=json.load(f)


def loop():
    lock = threading.Lock()
    print('thread %s is running...' % threading.current_thread().name)
    while(True):
        a=random.randint(0, 3783)
        if(map[str(a)]==0):
            lock.acquire()
            print('thread %s change %s' % (threading.current_thread().name,str(a)))
            map[a]=1
            lock.release()
            time.sleep(1)
        else:
            pass


print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
t=[]
for i in range(0,10):
    t.append(threading.Thread(target=loop,name="LoopThread "+str(i)))
for i in range(0,10):
    t[i].start()
# t[i].join()
print('thread %s ended.' % threading.current_thread().name)