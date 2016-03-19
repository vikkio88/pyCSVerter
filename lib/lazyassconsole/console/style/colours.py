class Colours:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    @staticmethod
    def from_string(name):
        if name in ('green', 'GREEN', 'Green', 'g'):
            return Colours.GREEN
        elif name in ('pink', 'PINK', 'Pink', 'p'):
            return Colours.PINK
        elif name in ('blue', 'Blue', 'Blue', 'b'):
            return Colours.BLUE
        elif name in ('yellow', 'YELLOW', 'Yellow', 'y'):
            return Colours.YELLOW
        elif name in ('red', 'RED', 'Red', 'r'):
            return Colours.RED
        else:
            return None
