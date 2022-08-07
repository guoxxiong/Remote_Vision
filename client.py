import socket
import cv2
import numpy as np
import gzip

def recv_all(s,count):
    buf=bytes()
    while count:
        newbuf = s.recv(count)
        if not newbuf:return None
        buf+=newbuf
        count-=len(newbuf)
    return buf

s = socket.socket()
host = socket.gethostname()
port = 2222

while True:
    try:
        s.connect(("10.32.11.199",port))
    except:
        print("有错误")
    else:
        break
        
count = 0
while True:
    data_len = recv_all(s,16)
    if len(data_len) == 16:
        stringData = recv_all(s, int(data_len))
        
        data = np.fromstring(stringData, dtype='uint8')
        
        tmp = cv2.imdecode(data, 1)  # 解码处理，返回mat图片
        
        img = cv2.resize(tmp, (320, 230))
        count = count + 1
        print(count)
        cv2.imshow('客户机', img)
    if cv2.waitKey(1) == 27:
        break
s.close()
