import vgamepad as vg

XboxKeyCodeMap = {
    "BTN_DPUP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "BTN_DPDOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "BTN_DPLEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "BTN_DPRIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "BTN_SELECT": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    "BTN_START": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    "BTN_THUMBL": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "BTN_THUMBR": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    "BTN_TL": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "BTN_TR": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "BTN_SOUTH": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "BTN_EAST": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "BTN_WEST": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "BTN_NORTH": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
}

class XboxGamepad:
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        self.gamepad.reset()
        gamepad.update()
        
    def PressKey(self, code):
        self.gamepad.press_button(button=code)
        self.gamepad.update()
        
    def ReleaseKey(self, code):
        self.gamepad.release_button(button=code)
        self.gamepad.update()
        
    def MoveLeftTrigger(self, val):
        self.gamepad.left_trigger(value=val)
        self.gamepad.update()
        
    def MoveRightTrigger(self, val):
        self.gamepad.right_trigger(value=val)
        self.gamepad.update()
        
    def MoveLeftJoystick(self, x, y):
        self.gamepad.left_joystick(x_value=x, y_value=y)
        self.gamepad.update()
        
    def MoveRightJoystick(self, x, y):
        self.gamepad.right_joystick(x_value=x, y_value=y)
        self.gamepad.update()
        
class DualshockGamepad:
    def __init__(self):
        self.gamepad = vg.VDS4Gamepad()
    