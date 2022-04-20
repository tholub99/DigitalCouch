import vgamepad as vg

XboxKeyCodeMap = {
    'BTN_DPUP': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    'BTN_DPDOWN': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    'BTN_DPLEFT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    'BTN_DPRIGHT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    'BTN_SELECT': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    'BTN_START': vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    'BTN_THUMBL': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    'BTN_THUMBR': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    'BTN_TL': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    'BTN_TR': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    'BTN_SOUTH': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'BTN_EAST': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    'BTN_WEST': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    'BTN_NORTH': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
}

XboxAbsCodeMap = {
    'ABS_Z': 'L_TRIGGER',
    'ABS_RZ': 'R_TRIGGER',
    'ABS_HAT0X': 'DPAD_HORIZONTAL',
    'ABS_HAT0Y': 'DPAD_VERTICAL',
    'ABS_Y': 'L_JOYSTICK_VERTICAL',
    'ABS_X': 'L_JOYSTICK_HORIZONTAL',
    'ABS_RY': 'R_JOYSTICK_VERTICAL',
    'ABS_RX': 'R_JOYSTICK_HORIZONTAL'
}

class XboxGamepad:
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        self.gamepad.reset()
        self.gamepad.update()
        
        self.LJ = [0,0]
        self.RJ = [0,0]
        
    def HandleEvent(self, ev_type, code, state):
        #Static Button
        if(ev_type == 'Key'):
                #keyPress
                if(state == 1):
                    self.PressKey(code)
                #keyRelease
                elif(state == 0):
                    self.ReleaseKey(code)
        #Varying Button           
        elif(ev_type == 'Absolute'):
            self.SetAbsInput(code, state) 
        
    def PressKey(self, code):
        self.gamepad.press_button(button=XboxKeyCodeMap[code])
        self.gamepad.update()
        
    def ReleaseKey(self, code):
        self.gamepad.release_button(button=XboxKeyCodeMap[code])
        self.gamepad.update()
    
    def SetAbsInput(self, code, state):
        code = XboxAbsCodeMap[code]
        if(code == 'DPAD_VERTICAL'):
            self.SetDPadY(state)
        elif(code == 'DPAD_HORIZONTAL'):
            self.SetDPadX(state)
        elif(code == 'L_TRIGGER'):
            self.SetLeftTrigger(state)
        elif(code == 'R_TRIGGER'):
            self.SetRightTrigger(state)
        elif(code == 'L_JOYSTICK_VERTICAL'):
            self.SetLeftJoystickY(state)
        elif(code == 'L_JOYSTICK_HORIZONTAL'):
            self.SetLeftJoystickX(state)
        elif(code == 'R_JOYSTICK_VERTICAL'):
            self.SetRightJoystickY(state)
        elif(code == 'R_JOYSTICK_HORIZONTAL'):
            self.SetRightJoystickX(state)
            
        self.gamepad.update()
    
    def SetDPadX(self, val):
        if(val == 0):
            self.gamepad.release_button(button=XboxKeyCodeMap['BTN_DPLEFT'])
            self.gamepad.release_button(button=XboxKeyCodeMap['BTN_DPRIGHT'])
        elif(val == 1):
            self.gamepad.press_button(button=XboxKeyCodeMap['BTN_DPRIGHT'])
        else:
            self.gamepad.press_button(button=XboxKeyCodeMap['BTN_DPLEFT'])
    
    def SetDPadY(self, val):
        if(val == 0):
            self.gamepad.release_button(button=XboxKeyCodeMap['BTN_DPDOWN'])
            self.gamepad.release_button(button=XboxKeyCodeMap['BTN_DPUP'])
        elif(val == 1):
            self.gamepad.press_button(button=XboxKeyCodeMap['BTN_DPDOWN'])
        else:
            self.gamepad.press_button(button=XboxKeyCodeMap['BTN_DPUP'])
        
            
    def SetLeftTrigger(self, val):
        self.gamepad.left_trigger(value=val)
        
    def SetRightTrigger(self, val):
        self.gamepad.right_trigger(value=val)
        
    def SetLeftJoystickX(self, x):
        self.gamepad.left_joystick(x_value=x, y_value=self.LJ[1])
        self.LJ[0] = x
        
    def SetLeftJoystickY(self, y):
        self.gamepad.left_joystick(x_value=self.LJ[0], y_value=y)
        self.LJ[1] = y
        
    def SetRightJoystickX(self, x):
        self.gamepad.right_joystick(x_value=x, y_value=self.RJ[1])
        self.RJ[0] = x
        
    def SetRightJoystickY(self, y):
        self.gamepad.right_joystick(x_value=self.RJ[0], y_value=y)
        self.RJ[1] = y
        
class DualshockGamepad:
    def __init__(self):
        self.gamepad = vg.VDS4Gamepad()
    