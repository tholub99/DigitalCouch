from gamepad import *

class Player:
    def __init__(self, gamepadType, inputSource):
        if(gamepadType == "xbox"):
            self.gamepad = XboxGamePad()
        elif(gamepadType == "dualshock"):
            self.gamepad = DualshockGamePad()
            