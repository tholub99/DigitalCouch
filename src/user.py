import gamepad

AVAILABLE_IDS = [7,6,5,4,3,2,1]

class User:
    def __init__(self, userID):
        self.userID = userID
        self.vPad = gamepad.XboxGamepad()
        
    def Input(self, inp):
        eventType = inp['type']
        eventCode = inp['code']
        eventState = int(inp['state'])
        
        self.vPad.HandleEvent(eventType, eventCode, eventState)
        
    def GetID(self):
        return self.userID