import cv2
import socket
import numpy as np
cap = cv2.VideoCapture(0)

s = socket.socket()
img_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]#opencv 图像清晰度，帧数
port = 2222

s.bind(("10.32.11.199",port)) #绑定ip地址和端口
s.listen(5)						#等待客户机连接
c,addr = s.accept()				#接受客户机连接
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame, (320,230))
    print("连接地址："+addr[0])
    _, img_encode = cv2.imencode('.jpg', frame, img_param)#opencv图像编码
    img_code = np.array(img_encode)
    img_data = img_code.tostring()#将数组格式转为字符串格式
    print(img_data)
    c.send(bytes(str(len(img_data)).ljust(16),encoding="utf8"))# 先发送数据的长度
    c.send(img_data)#再发送数据内容
    cv2.imshow("主机",frame)
    if cv2.waitKey(1)==27:
        c.close()
        break
