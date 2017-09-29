coding:utf-8
import socket
s=socket.socket()
s.connect(('127.0.0.1',1234))
print s.recv(1024)

dict={'title':'title1','content':'content1'}
s.send(str(dict))

s.close()

