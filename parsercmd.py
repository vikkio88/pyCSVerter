from cmd import Cmd
from parserconfig import config
import utils
from lib.lazyassconsole import Console


class ParserCmd(Cmd):
    prompt = '\n> '
    result_list = []

    def default(self, line):
        Console.print('Invalid command, type "help" for a list of commands')

    def do_quit(self, arg):
        """Quit and go back to the real word"""
        return True

    def do_parse(self, arg):
        """Parse and save the output to one of the configured ones"""
        if arg in config['output_formats']:
            utils.parse(arg)
        else:
            Console.print_red('Output format not supported, {}'.format(arg))
            utils.print_outputs()

    def do_load(self, arg):
        """Load the parsed and validated data from csv (you can specify a new file path)"""
        utils.load(arg)

    def do_reload(self, arg):
        """ReLoad the parsed and validated data from csv (you can specify a new file path)"""
        utils.load(arg)

    def do_sort(self, arg):
        """Sort by a field name: sort FIELD"""
        utils.order_by(arg)

    def do_save(self, arg):
        """save the List parsed on one of the output: save json"""
        utils.save(arg)

    def do_outputs(self, arg):
        """Print available output formats"""
        utils.print_outputs()

    def do_print(self, arg):
        """Print the whole parsed/validated list or one element: print 1"""
        utils.print_list(arg)

    def do_results_info(self, args):
        """Print a set of info about the results, if they are loaded"""
        utils.results_info()
