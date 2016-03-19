from lib.helpers.formatters.iformatter import IFormatter
import json


class JsonFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'json'

    def str_dump(self, dictionary, filename):
        str_out = json.dumps(dictionary)
        with open(filename, mode='w') as f:
            f.write(str_out)
