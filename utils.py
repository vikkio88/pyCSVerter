from parserconfig import config
import pycsverter
from lib.lazyassconsole import Console
from lib.helpers.csvimporter import CsvImporter
from lib.helpers.datavalidator import DataValidator
from lib.helpers.outputdumper import OutputDumper
import os.path


def print_banner():
    print(config['banner'])
    print(config['help_message'])


def parse(output, file_path=None):
    output_file_name = '{}.{}'.format(config['output_file_name'], output)
    Console.print('converting csv data in {}'.format(output), 'g')
    if file_path is None:
        file_path = config['default_file']

    if os.path.isfile(file_path):
        if len(pycsverter.result_list) == 0:
            parsed = import_from_csv(file_path)
            validate_dict(parsed)
        Console.print_yellow('Printing output ({}), on file {}'.format(output, output_file_name))
        OutputDumper.dump(pycsverter.result_list, output, output_file_name)
        Console.print_green('Done!')
    else:
        Console.print_red(
            'File not found in path {}, please specify a valid filePath'.format(file_path))


def import_from_csv(file_path):
    Console.print_yellow('Parsing {}...'.format(file_path))
    parsed = CsvImporter.csv_to_dictlist(file_path)
    parsed = convert_star_to_int(parsed)
    Console.print_green('Parsed!')
    return parsed


def validate_dict(parsed):
    Console.print_yellow('Validating data')
    validated = DataValidator.validate(parsed)
    Console.print_green('Validated!')
    pycsverter.result_list = validated
    Console.print_yellow('Result List saved in memory')


def print_outputs():
    """ Prints the accepted/configured outputs """
    Console.print_green('Output supported:')
    for output in config['output_formats']:
        Console.print_blue(output)


def convert_star_to_int(parsed):
    """ this function is mostly a workaround because the csv class read everything to string
    :param parsed:
    """
    for row in parsed:
        stars = row.get('stars', '0')
        if not isinstance(stars, int):
            if stars == '':
                stars = '0'
            row['stars'] = int(stars)
    return parsed


def save(output):
    """ saves the result list to file
    :param output:
    """
    output_file_name = '{}.{}'.format(config['output_file_name'], output)
    if len(pycsverter.result_list) == 0:
        Console.print_red('Parsed result not found, reloading...')
        load()
    Console.print_yellow('Printing output ({}), on file {}'.format(output, output_file_name))
    OutputDumper.dump(pycsverter.result_list, output, output_file_name)
    Console.print_green('Done!')


def order_by(field_name):
    """ this function sorts the result list (reverse order if sorted already)
    :param field_name:
    """
    if len(pycsverter.result_list) == 0:
        Console.print_red('Parsed result not found, reloading...')
        load()
    if field_name in pycsverter.result_list[0]:
        Console.print_yellow('Sorting list by {}'.format(field_name))
        pycsverter.result_list.sort(key=lambda x: x[field_name])
        Console.print_green('Done!')
    else:
        Console.print_red('Field {} not in result list:')
        Console.print_blue('Fields available:')
        for k in pycsverter.result_list[0]:
            Console.print_blue(k)


def print_list(index=None):
    """ prints the result list or just one element
    :param index:
    """
    if len(pycsverter.result_list) == 0:
        Console.print_red('Parsed result not found, reloading...')
        load()
    if index == '':
        index = None
    if index is None:
        print(pycsverter.result_list)
        Console.print_green('Printed all list')
    else:
        try:
            index = int(index)
        except ValueError:
            Console.print_red("{} is not a valid int, nice try!\n index set to 0".format(index))
            index = 0
        if index <= len(pycsverter.result_list):
            print(pycsverter.result_list[index])
            Console.print_green('Printed element {}'.format(index))


def load(file_path=None):
    """ load the result_list form the csv file
    :param file_path:
    """
    if file_path == '' or file_path is None:
        file_path = config['default_file']

    if os.path.isfile(file_path):
        parsed = import_from_csv(file_path)
        validate_dict(parsed)
    else:
        Console.print_red(
            'File not found in path {}, please specify a valid filePath'.format(file_path))


def results_info():
    """ prints info about the result list """
    if len(pycsverter.result_list) == 0:
        Console.print_red('Parsed result not found...run: load')
    else:
        Console.print_blue('List of {} elements'.format(len(pycsverter.result_list)))
