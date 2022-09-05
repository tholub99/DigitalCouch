from inputs import get_gamepad
from inputs import devices
from player import Player
from threading import Thread, Lock, Timer
import gamepad
import networking
import time
import socket

class Host:
    def __init__(self):
        self.players = []

def Server():
    server = networking.Server()
def Client():
    #ip = input('Server IP -> ')
    #port = int(input('Server Port -> '))
    client = networking.Client(socket.gethostname(), 5000)
    
    
    for device in devices:
        print(device)

    eventThread = Thread(target=EventThread, args=(client,))

    eventThread.start()
    
    eventThread.join()
    client.Close();
    
def Test():
    """Just print out some event infomation when the gamepad is used."""
    for device in devices:
        print(device)
    clientThread = Thread(target=ClientTestThread, args=())
    eventThread = Thread(target=EventTestThread, args=())
    
    eventThread.start()
    clientThread.start()
    
    eventThread.join()
    clientThread.join()
    
    
    '''while 1:
        events = get_gamepad()

        for event in events:
            if(event.ev_type == 'Sync'):
                continue
            #Account for Joystick wobble
            skipEvent = False
            if(event.code in AbsPrevEvent.keys()):
                event.state = NegateJoyWobble(event)
                if(AbsPrevEvent[event.code] != None):
                    skipEvent = IsDuplicateEvent(event)
                else:
                    AbsPrevEvent[event.code] = event.state
                
                    
            if(not skipEvent):
                print(event.ev_type, event.code, event.state)'''

RecentEvents = {}
lock = Lock()

def EventTestThread():
    global RecentEvents
    global lock
    while True:
        events = get_gamepad()
        for event in events:
            if(event.ev_type == 'Sync'):
                continue
            #Account for Joystick wobble
            skipEvent = False
            if(event.code in AbsPrevEvent.keys()):
                event.state = NegateJoyWobble(event)
                if(AbsPrevEvent[event.code] != None):
                    skipEvent = IsDuplicateEvent(event)
                else:
                    AbsPrevEvent[event.code] = event.state
                    
                if(not skipEvent):
                    with lock:
                        RecentEvents[event.code] = event
                continue
                
            print(event.ev_type, event.code, event.state)

def ClientTestThread():
    global RecentEvents
    global lock
    while True:
        #print(RecentEvents)
        with lock:
            events = list(RecentEvents.values())
            RecentEvents.clear()
        for event in events:
            print(event.ev_type, event.code, event.state)
        time.sleep(0.1)

def EventThread(client):
    global RecentEvents
    #global lock
    global sendAbs
    
    sendAbs = True
    
    while True:
        
        #Send Recent ABS Event
        if(sendAbs):
            sendAbs = False
            events = list(RecentEvents.values())
            RecentEvents.clear()
        
            for event in events:
                client.SendEventMessageToServer(event)
                print(event.ev_type, event.code, event.state)
            unblockAbs = Timer(0.1, AllowAbsSend)
            unblockAbs.start()
        
        
        events = get_gamepad()
        #print(events)
        for event in events:
            if(event.ev_type == 'Sync'):
                continue
            #Account for Joystick wobble
            skipEvent = False
            if(event.code in AbsPrevEvent.keys()):
                event.state = NegateJoyWobble(event)
                if(AbsPrevEvent[event.code] != None):
                    skipEvent = IsDuplicateEvent(event)
                else:
                    AbsPrevEvent[event.code] = event.state
                    
                if(not skipEvent):
                        RecentEvents[event.code] = event
                continue
            
            #Send KEY Event
            client.SendEventMessageToServer(event)
            print(event.ev_type, event.code, event.state)
            
def AllowAbsSend():
    global sendAbs
    sendAbs = True

AbsPrevEvent = {
    'ABS_Y': None,
    'ABS_X': None,
    'ABS_RY': None,
    'ABS_RX': None
}

def IsDuplicateEvent(event):
    if(abs(event.state - AbsPrevEvent[event.code]) <= 100):
        return True
    AbsPrevEvent[event.code] = event.state
    return False
    
def NegateJoyWobble(event):
    if(abs(event.state) <= 5000):
        return 0
    return event.state

if __name__ == "__main__":
    inp = int(input('1 - Server\n2 - Client\n3 - Test\n-> '))
    #Run Server
    while inp < 0 or inp > 3:
        inp = int(inp('-> '))
    if(inp == 1):
        Server()
    #Run Client
    elif(inp == 2):
        Client()
    #Test Components
    elif(inp == 3):
        Test()