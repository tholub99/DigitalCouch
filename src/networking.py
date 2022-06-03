import socket
import user
import json
from inputs import get_gamepad
from inputs import devices

HDR_SIZE = 31
SIZE = 1024

class Server:
    def __init__(self):
        self.ip = socket.gethostname()
        self.port = 5000
        self.clients = {}
        self.Run()
        
    def Run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)
        
        print('Server Started on', self.ip + ':' + str(self.port))
        
        conn, addr = self.sock.accept()
        while True:
            dataType, dataSize = self.ReadHeader(conn)
            data = conn.recv(dataSize)
            data = data.decode('utf-8')
            dataJson = json.loads(data)
            
            #Alert Message
            if dataType == 'alert':
                
                if(dataJson['alert'] == 'New Client') and not (addr in self.clients.keys()):
                    if(user.AVAILABLE_IDS != []):
                        self.clients[addr] = user.User(user.AVAILABLE_IDS.pop())
            
                elif(dataJson['alert'] == 'Client Disconnecting') and (addr in self.clients.keys()):
                    user.AVAILABLE_IDS.append(self.clients[addr].GetID())
                    self.clients.pop(addr)
            
            elif dataType == 'event':
                if(addr in self.clients.keys()):
                    self.clients[addr].Input(dataJson)
                
            print('Message from: ' + str(addr))
            print('From connected user: ' + data)
            
        conn.close()
        self.Close()
        
    def ReadHeader(self, conn):
        hdr = conn.recv(HDR_SIZE)
        hdr = hdr.decode('utf-8')
        print(hdr)
        hdrJson = json.loads(hdr)
        return hdrJson['type'], int(hdrJson['size'])
    
    def Close(self):
        self.sock.close()

class Client:
    def __init__(self, ip, port):
        self.server = (ip, port)
        self.Connect()
        
    def Connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.server)
        
        msg = GenerateAlertMessage('New Client').encode('utf-8')
        hdr = GenerateHeader('alert', len(msg)).encode('utf-8')
        
        self.sock.send(hdr)
        self.sock.send(msg)
        
    def Close(self):
        msg = GenerateAlertMessage('Client Disconnecting').encode('utf-8')
        hdr = GenerateHeader('alert', len(msg)).encode('utf-8')
        
        self.sock.send(hdr)
        self.sock.send(msg)
        
        self.sock.close()
    
    def SendEventMessageToServer(self, event):
        msg = GenerateEventMessage(event.ev_type, event.code, event.state).encode('utf-8')
        hdr = GenerateHeader('event', len(msg)).encode('utf-8')
        
        self.sock.send(hdr)
        self.sock.send(msg)


def GenerateHeader(msgType, size):
    length = str(size).zfill(2)
        
    hdrJson = {
        'type': msgType,
        'size': length
    }
    hdr = json.dumps(hdrJson)
    return hdr

def GenerateEventMessage(ev_type, code, state):
    msgJson = {
       'type': ev_type,
       'code': code,
       'state': state
    }
    
    msg = json.dumps(msgJson)
    return msg

def GenerateAlertMessage(alert):
    msgJson = {
       'alert': alert
    }
    
    msg = json.dumps(msgJson)
    return msg
    


if __name__ == '__main__':
    inp = int(input('1 - Server\n2 - Client\n-> '))
    #Run Server
    if(inp == 1):
        server = Server()
    #Run Client
    elif(inp == 2):
        #ip = input('Server IP -> ')
        #port = int(input('Server Port -> '))
        client = Client('192.168.0.11', 5000)
        
        for device in devices:
            print(device)
        while True:
            events = get_gamepad()
            for event in events:
                eventMsg = event.ev_type + '|' + event.code + '|' + str(event.state)
                client.SendMessageToServer(eventMsg)
                print(event.ev_type, event.code, event.state)
        client.Close();
    #Check Msg Generators
    elif(inp == 3):
        msg = GenerateEventMessage('Key', 'BTN_SOUTH', 0).encode('utf-8')
        print(msg)
        print(len(msg))
        hdr = GenerateHeader('event', len(msg)).encode('utf-8')
        print(hdr)
        print(len(hdr))
        
        
        