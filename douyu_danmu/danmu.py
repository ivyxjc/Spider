import socket
import hashlib
import time
import uuid

room_status = {
    "sd_rmtp_url": None,
    "hd_rmtp_url": None,
    "spd_rmtp_url": None,
    "id": 67373,
    "name": None,
    "gg_show": None,
    "owner_uid": None,
    "owner_name": None,
    "room_url": None,
    "near_show_time": None,
    "username": None,
    "tags": None,
    "live_stat": None,
    "fans_count": None,
    "weight": None,
    "is_finished": False  # 当标记为 True的时候,这个时候所有的
}

class DanmuManager(object):
    def __init__(self,auth_dst_ip, auth_dst_port):
        self.DANMU_ADDR = ("danmu.douyutv.com", 8602)

        self.DANMU_AUTH_ADDR = (auth_dst_ip, int(auth_dst_port))

        self.danmu_auth_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.danmu_auth_socket.connect(self.DANMU_AUTH_ADDR)

        self.danmu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.danmu_socket.connect(self.DANMU_ADDR)

        self.room_id = str(room_status["id"])
        self.auth_dst_ip = auth_dst_ip
        self.auth_dst_port = auth_dst_port
        self.dev_id = str(uuid.uuid4()).replace("-", "")


    def send_danmu_loginreq_msg(self):
        data = "type@=loginreq/username@=" + self.username + "/password@=1234567890123456/roomid@=" + self.room_id + "/"
        msg = self.message(data)
        self.danmu_socket.sendall(msg)

    def send_auth_loginreq_msg(self):
        time = self.timestamp()
        vk = hashlib.md5(bytes(time + "7oE9nPEG9xXV69phU31FYCLUagKeYtsF" + self.dev_id, 'utf-8')).hexdigest()
        data = "type@=loginreq/username@=/ct@=0/password@=/roomid@=" + self.room_id + "/devid@=" + self.dev_id + "/rt@=" + self.timestamp() + "/vk@=" + vk + "/ver@=20150929/"
        msg = self.message(data)
        self.danmu_auth_socket.sendall(msg)

    def timestamp(self):
        return str(int(time.time()))