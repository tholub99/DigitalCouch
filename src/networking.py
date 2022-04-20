import socket

SIZE = 1024

class Host:
    def __init__(self):
        self.ip = '192.168.0.11'
        self.port = 5000
        self.clients = {}
        self.RunServer()
        
    def RunServer(self):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind((self.ip, self.port))
        
        print('Server Started on', self.ip + ':' + str(self.port))
        while True:
            data, addr = mySocket.recvfrom(SIZE)
            data = data.decode('utf-8')
            print('Message from: ' + str(addr))
            print('From connected user: ' + data)
        mySocket.close()

class Client:
    def __init__(self, ip, port):
        self.server = (ip, port)
        
    def ConnectToHost(self):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = input('-> ')
        while msg != 'q':
            mySocket.sendto(msg.encode('utf-8'), self.server)
            print("Message sent to server")
            msg = input('-> ')
        mySocket.close()
        
if __name__ == '__main__':
    inp = int(input('1 - Host\n2 - Client\n-> '))
    if(inp == 1):
        host = Host()
    elif(inp == 2):
        ip = input('Server IP -> ')
        port = int(input('Server Port -> '))
        client = Client(ip, port)