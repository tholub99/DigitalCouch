from inputs import get_gamepad
from inputs import devices
from player import Player
from threading import Thread, Lock
import gamepad
import networking
import time

class Host:
    def __init__(self):
        self.players = []

def Server():
    server = networking.Server()
def Client():
    #ip = input('Server IP -> ')
    #port = int(input('Server Port -> '))
    client = networking.Client('192.168.0.11', 5000)
    
    for device in devices:
        print(device)
    clientThread = Thread(target=ClientThread, args=(client,))
    eventThread = Thread(target=EventThread, args=())

    eventThread.start()
    clientThread.start()
    
    eventThread.join()
    clientThread.join()
    client.Close();
    
def Test():
    #vPad = gamepad.XboxGamepad()
    """Just print out some event infomation when the gamepad is used."""
    for device in devices:
        print(device)
    clientThread = Thread(target=ClientTestThread, args=())
    eventThread = Thread(target=EventThread, args=())
    
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

def EventThread():
    global RecentEvents
    global lock
    while True:
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
                with lock:
                    RecentEvents[event.code] = event
        #print(RecentEvents)

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
        time.sleep(0.05)
        
def ClientThread(client):
    global RecentEvents
    global lock
    while True:
        #print(RecentEvents)
        with lock:
            events = list(RecentEvents.values())
            RecentEvents.clear()
        for event in events:
            eventMsg = event.ev_type + '|' + event.code + '|' + str(event.state)
            client.SendMessageToServer(eventMsg)
            
            print(event.ev_type, event.code, event.state)
            
        time.sleep(0.05)

AbsPrevEvent = {
    'ABS_Y': None,
    'ABS_X': None,
    'ABS_RY': None,
    'ABS_RX': None
}

def IsDuplicateEvent(event):
    if(abs(event.state - AbsPrevEvent[event.code]) <= 10):
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