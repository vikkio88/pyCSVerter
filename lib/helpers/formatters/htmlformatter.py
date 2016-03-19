from lib.helpers.formatters.iformatter import IFormatter


class HtmlFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'html'

    def str_dump(self, dictionary, filename):
        result = '<table><tr>'
        for val in dictionary[0].keys():
            result += '<th>{}</th>'.format(val)
        result += '</tr>'
        for d in dictionary:
            result += '<tr>'
            for val in d.values():
                result += '<td>{}</td>'.format(val)
            result += '</tr>'
        with open(filename, mode='w') as f:
            f.write(result)
