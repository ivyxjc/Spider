import socket
import hashlib
import time
import uuid
from douyu_danmu.models.douyu_msg import DouyuMsg

"""
type 表示消息的类型登陆消息为loginreq
username 不需要，请求登陆以后系统会自动的返回对应的游客账号。
ct 不清楚什么意思，默认为0并无影响
password 不需要
roomid 房间的id
devid 为设备标识，无所谓，所以我们使用随机的UUID生成
rt 应该是runtime吧，时间戳
vk 为时间戳+"7oE9nPEG9xXV69phU31FYCLUagKeYtsF"+devid的字符串拼接结果的MD5值（这个是参考了一篇文章，关于这一处我也不大明白怎么探究出来的）
ver 默认

以上data数据格式来自于知乎用户曹童童的回答。链接：https://www.zhihu.com/question/29027665/answer/85530089
"""

danmu_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
danmu_socket.connect(("danmu.douyutv.com",8601))

dev_id=str(uuid.uuid4()).replace("-", "")

vk = hashlib.md5(bytes(str(int(time.time())) + "7oE9nPEG9xXV69phU31FYCLUagKeYtsF" + dev_id, 'utf-8')).hexdigest()
data = "type@=loginreq/username@=/ct@=0/password@=/roomid@=" \
       + str(67373) \
       + "/devid@=" \
       + dev_id \
       + "/rt@=" \
       + str(int(time.time())) \
       + "/vk@=" \
       + vk \
       + "/ver@=20150929/"

a=DouyuMsg(data).get_bytes()

danmu_socket.sendall(a)
danmu_data=danmu_socket.recv(4000)
print(danmu_data)


class DanmuManager(object):
    def __init__(self):
        pass

