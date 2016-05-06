# coding:utf-8
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 10080
MESSAGE = 'Hello, world!'

print 'UDP 目标IP：', UDP_IP
print 'UDP 目标端口：', UDP_PORT
print '发送的内容：', MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
