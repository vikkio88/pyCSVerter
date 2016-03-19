from lib.helpers.formatters.iformatter import IFormatter


class YamlFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'yaml'

    def str_dump(self, dictionary, filename):
        result = '---\n'
        for d in dictionary:
            result += '-'
            i = 0
            for k, v in d.items():
                if i == 0:
                    result += ' {} : {}\n'.format(k, v)
                else:
                    result += '  {} : {}\n'.format(k, v)
                i += 1

        result += '\n'
        with open(filename, mode='w') as f:
            f.write(result)
