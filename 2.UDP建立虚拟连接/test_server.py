#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/5/11 下午3:54
#   Desc    :   server

import socket
import time

UDP_IP = ''
UDP_PORT = 5000
_ID = []  # 存储建立连接的protocol_id
_IP = None  # 存储建立连接的IP和端口
TIME_OUT = 1  # 超时时间

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(TIME_OUT)

def check_protocol_id(protocol_id, _ID):
	'''
	检测protocol_id
	'''
	if _ID:
		if protocol_id in _ID:
			return True
		else:
			return False
	else:
		_ID.append(protocol_id)
		return True

print '准备接收内容。'
while 1:
	try:
		response = ''
		data, addr = sock.recvfrom(1024)  # 缓冲区大小为1024bytes
		protocol_id, data = data.split('|')
		if _IP:
			if _IP == addr:
				response = '建立连接'
				print '从{ip}:{port}，接收到内容：{data}'.format(ip=addr[0],
															   port=addr[1], data=data)
			else:
				response = '无法建立连接'
		else:
			if check_protocol_id(protocol_id, _ID):
				_IP = addr
				response = '建立连接'
				print '从{ip}:{port}，接收到内容：{data}'.format(ip=addr[0],
															   port=addr[1], data=data)
			else:
				response = '无法建立连接'
		time.sleep(2)
		# 返回响应数据包给客户端
		sock.sendto(response, addr)
	except socket.timeout:
		print '连接超时，注销连接，其他socket可以连入'
		_IP = None
		_ID = []
