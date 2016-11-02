import socket

socket=socket.socket()

socket.connect(("danmu.douyutv.com",12601))
msg_1 = "type@=loginreq/username@=visitor164621/password@=1234567890123456/roomid@=67373/."

socket.send(bytes(msg_1,encoding='utf8'))
a=socket.recv(4096)
print(a)
