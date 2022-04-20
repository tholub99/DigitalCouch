from inputs import get_gamepad
from inputs import devices
from player import Player
import gamepad

class Host:
    def __init__(self):
        self.players = []

def main():
    vPad = gamepad.XboxGamepad()
    """Just print out some event infomation when the gamepad is used."""
    for device in devices:
        print(device)
    while 1:
        events = get_gamepad()
        for event in events:       
            vPad.HandleEvent(event.ev_type, event.code, event.state)
            print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    main()