from .formatters.config import formatters


class OutputDumper(object):
    @staticmethod
    def dump(content, out_format, filename):
        if out_format in formatters:
            formatter = formatters.get(out_format)
            formatter.str_dump(formatter, content, filename)
        else:
            raise Exception('Error: no formatter')
