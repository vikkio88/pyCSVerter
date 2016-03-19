from lib.helpers.formatters.iformatter import IFormatter
import sqlite3


class SqliteFormatter(IFormatter):
    def __init__(self):
        self.output_format = 'sqlite'

    def str_dump(self, dictionary, filename):
        elements = ''
        i = 1
        keys = dictionary[0].keys()
        count = len(keys)
        for head in keys:
            elements += head
            if i != count:
                elements += ','
            i += 1
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute('''CREATE TABLE hotels
             ({})'''.format(elements))
        conn.commit()

        for d in dictionary:
            elements = ''
            i = 1
            values = d.values()
            count = len(values)
            for val in values:
                elements += '\'' + (str(val)).replace("'", "") + '\''
                if count != i:
                    elements += ','
                i += 1
            c.execute("INSERT INTO hotels VALUES ({})".format(elements))
            conn.commit()

        conn.close()
