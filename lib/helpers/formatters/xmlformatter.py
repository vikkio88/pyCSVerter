from lib.helpers.formatters.iformatter import IFormatter
from vendors.dicttoxml.dicttoxml import dicttoxml


class XmlFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'xml'

    def str_dump(self, dictionary, filename):
        xml = dicttoxml(dictionary)
        with open(filename, mode='wb') as f:
            f.write(xml)
