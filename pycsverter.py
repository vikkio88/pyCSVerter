from utils import *
from parsercmd import ParserCmd

"""Application Entry point"""

"""This is the list which will hold the result"""
result_list = []


def main():
    """App Main flow"""
    print_banner()
    ParserCmd().cmdloop()


if __name__ == '__main__':
    main()
