import sys
import os
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
import time
import threading

SERVER_IP   = 'localhost'
SIZE = 1024

def sender():
    print ("partito")
    PORT_NUMBER = 5000
    print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
    mySocket = socket( AF_INET, SOCK_DGRAM )
    i = 0
    while True:
        myMessage = 'echo Tutto bene - {}'.format(i+1)
        mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        time.sleep(0.8)
        i = i + 1
    return 0

def listener():
    PORT_NUMBER = 6000
    hostName = gethostbyname( '0.0.0.0' )
    mySocket = socket( AF_INET, SOCK_DGRAM )
    mySocket.bind( (hostName, PORT_NUMBER) )
    print ("Test server listening on port {0}\n".format(PORT_NUMBER))
    while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        os.system(data.decode('UTF-8'))

def main():
    thread1 = threading.Thread(target=sender, name='Thread1')
    thread2 = threading.Thread(target=listener, name='Thread2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    time.sleep(10)
    sys.exit()
if __name__ == '__main__':main()




