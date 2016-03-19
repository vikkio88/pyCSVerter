class Style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def from_string(name):
        if name in ('bold', 'BOLD', 'Bold', 'b'):
            return Style.BOLD
        elif name in ('underline', 'UNDERLINE', 'Underline', 'u'):
            return Style.UNDERLINE

