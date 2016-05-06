# coding:utf-8
import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 10080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print '准备接收内容。'
while 1:
	data, addr = sock.recvfrom(1024)  # 缓冲区大小为1024bytes
	print '从{ip}:{port}，接收到内容：{data}'.format(ip=addr[0],
												   port=addr[1], data=data)
