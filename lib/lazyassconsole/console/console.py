from lib.lazyassconsole.console.style.style import Style as St
from lib.lazyassconsole.console.style.styleutils import StyleUtils as Su
from lib.lazyassconsole.console.style.colours import Colours as Co


class Console:
    @staticmethod
    def print_yellow(message):
        print((Co.YELLOW + message + Su.ENDC))

    @staticmethod
    def print_blue(message):
        print((Co.BLUE + message + Su.ENDC))

    @staticmethod
    def print_red(message):
        print((Co.RED + message + Su.ENDC))

    @staticmethod
    def print_green(message):
        print((Co.GREEN + message + Su.ENDC))

    @staticmethod
    def print_pink(message):
        print((Co.PINK + message + Su.ENDC))

    @staticmethod
    def format_text(message, colour=None, style=None):
        if colour is not None and style is not None:
            return "{}{}{}{}".format(St.from_string(style), Co.from_string(colour), message, Su.ENDC)
        elif colour is not None and style is None:
            return "{}{}{}".format(Co.from_string(colour), message, Su.ENDC)
        elif colour is None and style is not None:
            return "{}{}{}".format(St.from_string(colour), message, Su.ENDC)

    @staticmethod
    def print(message, colour=None, style=None):
        print(Console.format_text(message, colour, style))
