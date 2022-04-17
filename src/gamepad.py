import vgamepad as vg

xboxButtonMap = {
    "dpadUp": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "dpadDown": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "dpadLeft": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "dpadRight": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "start": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    "back": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    "leftThumb": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "rightThumb": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    "leftShoulder": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "rightShoulder": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "guide": vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
    "a": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "b": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "x": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
}

class XboxGamepad:
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        
    def PushButton(self, button):
        self.gamepad
        
class DualshockGamepad:
    def __init__(self):
        self.gamepad = vg.VDS4Gamepad()
    