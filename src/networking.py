import socket
import user
from inputs import get_gamepad
from inputs import devices

SIZE = 1024

class Server:
    def __init__(self):
        self.ip = '192.168.0.11'
        self.port = 5000
        self.clients = {}
        self.Run()
        
    def Run(self):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind((self.ip, self.port))
        
        print('Server Started on', self.ip + ':' + str(self.port))
        while True:
            data, addr = mySocket.recvfrom(SIZE)
                
            data = data.decode('utf-8')
            if(data.startswith('New Client') and not (addr in self.clients.keys())):
                if(user.AVAILABLE_IDS != []):
                    self.clients[addr] = user.User(user.AVAILABLE_IDS.pop())
            
            elif(data.startswith('Client Disconnecting') and (addr in self.clients.keys())):
                user.AVAILABLE_IDS.append(self.clients[addr].GetID())
                self.clients.pop(addr)
            
            elif(addr in self.clients.keys()):
                self.clients[addr].Input(data)
                
            print('Message from: ' + str(addr))
            print('From connected user: ' + data)
            
            
        self.Close()
    
    def Close(self):
        mySocket.close()

class Client:
    def __init__(self, ip, port):
        self.server = (ip, port)
        self.Open()
        
    def Open(self):
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        msg = 'New Client'
        self.mySocket.sendto(msg.encode('utf-8'), self.server)
        
    def Close(self):
        msg = 'Client Disconnecting'
        self.mySocket.sendto(msg.encode('utf-8'), self.server)
        self.mySocket.close()
    
    def SendMessageToServer(self, msg):
        self.mySocket.sendto(msg.encode('utf-8'), self.server)
        
if __name__ == '__main__':
    inp = int(input('1 - Server\n2 - Client\n-> '))
    #Run Server
    if(inp == 1):
        server = Server()
    #Run Client
    elif(inp == 2):
        ip = input('Server IP -> ')
        port = int(input('Server Port -> '))
        client = Client(ip, port)
        
        for device in devices:
            print(device)
        while True:
            events = get_gamepad()
            for event in events:
                eventMsg = event.ev_type + '|' + event.code + '|' + str(event.state)
                client.SendMessageToServer(eventMsg)
                print(event.ev_type, event.code, event.state)
        client.Close();