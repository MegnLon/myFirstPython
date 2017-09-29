#!/usr/bin/env python
#coding:utf-8


# taskkill /f /im python.exe
import socket
s=socket.socket()
#host = socket.gethostname()
s.bind(('127.0.0.1',1234))
#s.bind((host,1234))

s.listen(5)
while True:
	c, addr=s.accept()
	print u"连接地址为：",addr
	c.send('成功链接至服务器端....')
	dict=eval(c.recv(1024))
	if dict:
		print u'收到的数据为：',dict
		print u"日记的标题为：",dict['title']
		print u"日记的内容为：",dict['content']

	c.close()