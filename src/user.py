import gamepad

AVAILABLE_IDS = [7,6,5,4,3,2,1]

class User:
    def __init__(self, userID):
        self.userID = userID
        self.vPad = gamepad.XboxGamepad()
        
    def Input(self, inp):
        self.vPad.HandleInput(inp)
        
    def GetID(self):
        return self.userID