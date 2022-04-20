import gamepad

AVAILABLE_IDS = [7,6,5,4,3,2,1]

class User:
    def __init__(self, userID):
        self.userID = userID
        self.vPad = gamepad.XboxGamepad()
        
    def Input(self, inp):
        event = inp.split('|')
        eventType = event[0]
        eventCode = event[1]
        eventState = int(event[2])
        
        self.vPad.HandleEvent(eventType, eventCode, eventState)
        
    def GetID(self):
        return self.userID