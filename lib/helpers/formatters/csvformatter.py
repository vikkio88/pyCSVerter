from lib.helpers.formatters.iformatter import IFormatter
import csv


class CsvFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'csv'

    def str_dump(self, dictionary, filename):
        keys = dictionary[0].keys()
        with open(filename, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dictionary)
