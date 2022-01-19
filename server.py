import socket
import threading

HOST = ''
PORT = int(input("PORT #: "))
ADDR = (HOST, PORT)
BUFSIZ = 1024

def send(sock):
    while True:
        sendData = input('>> ')
        sock.send(bytes('server: %s' % (sendData), 'utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(BUFSIZ)
        print(recvData.decode())

servSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servSock.bind(ADDR)
servSock.listen(5) 

print('waiting for connection...')
cliSock, addr = servSock.accept()
print('...connected from :', addr)

sender = threading.Thread(target=send, args=(cliSock,))
receiver = threading.Thread(target=receive, args=(cliSock,))

sender.start()
receiver.start()