import socket
import threading

HOST = input('Host IP: ')
PORT = int(input('PORT #: '))
ADDR = (HOST, PORT)
BUFSIZ = 1024

def send(sock):
    while True:
        sendData = input('>> ')
        sock.send(bytes('client: %s' % (sendData), 'utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(BUFSIZ)
        print(recvData.decode())


cliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliSock.connect(ADDR)

print('Connected..')

sender = threading.Thread(target=send, args=(cliSock,))
receiver = threading.Thread(target=receive, args=(cliSock,))

sender.start()
receiver.start()