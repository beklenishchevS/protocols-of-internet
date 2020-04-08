import socket

sock = socket.socket()
sock.connect(('smtp.yandex.ru', 587))

data = sock.recv(256)
print(data)
sock.send(b'EHLO x\n')
data = sock.recv(256)
print(data)
sock.send(b'AUTH LOGIN\n')
data = sock.recv(256)
sock.close()

print(data)