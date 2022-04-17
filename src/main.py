from inputs import get_gamepad
from inputs import devices
from player import Player

class Host:
    def __init__(self):
        self.players = []

def main():
    """Just print out some event infomation when the gamepad is used."""
    for device in devices:
        print(device)
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    main()