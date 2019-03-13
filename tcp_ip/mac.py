#!/usr/bin/python

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.0.1.33', 8081))

#print(s.recv(1024).decode('utf-8'))

#for data in [b'Michale', b'Tracy', b'Bob']:
for data in [b'00:0c:29:93:8e:32']:
    s.send(data)
#    print(s.recv(1024).decode('utf-8'))
#s.send(b'exit')
s.close()


