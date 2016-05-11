#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/5/11 下午3:54
#   Desc    :   client
import socket
import time
import hashlib

UDP_IP = ''
UDP_PORT = 5000
MESSAGE = 'Hello, world!'
TIME_OUT = 3

print 'UDP 目标IP：', UDP_IP
print 'UDP 目标端口：', UDP_PORT
print '发送的内容：', MESSAGE

class Udp(object):
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = None
        # 设置超时时间
		self.socket.settimeout(TIME_OUT)

	@property
	def protocol_id(self):
		hash = hashlib.md5(str(time.time()) + 'xueweihan')
		return hash.hexdigest()

	def send_mesaage(self):
		# 这里只简单用｜分割protocol_id和发送内容
		message = self.protocol_id +'|'+ MESSAGE
		self.socket.sendto(message, (UDP_IP, UDP_PORT))

	def get_message(self):
		data, addr = self.socket.recvfrom(1024)
		if self.server_addr:
			# 客户端也只接收建立连接的服务端的数据包
			if self.server_addr == addr:
				return data
			else:
				return None
		else:
			self.server_addr = addr
			return data

s1 = Udp()
for i in range(2):
	try:
		s1.send_mesaage()
		print s1.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s1.server_addr = None


s2 = Udp()
for i in range(2):
# 此时是无法建立连接的，因为上一个连接还没有销毁
	try:
		s2.send_mesaage()
		print s2.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s2.server_addr = None

time.sleep(2)
s3 = Udp()
for i in range(2):
# 此时是可以建立连接的，因为上面连接以超时
	try:
		s3.send_mesaage()
		print s3.get_message()
	except socket.timeout:
		print '连接超时'
		# 清除原来建立连接的数据
        s3.server_addr = None
