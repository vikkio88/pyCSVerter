import csv


class CsvImporter(object):
    @staticmethod
    def csv_to_dictlist(filename):
        with open(filename, mode='r') as f:
            reader = csv.reader(f)
            keys = []
            list = []
            i = 0
            for row in reader:
                if i == 0:
                    keys = row
                else:
                    list.append(row)
                i += 1

            dictlist = []

            for elem in list:
                d = {}
                i = 0
                for key in keys:
                    val = None
                    try:
                        val = elem[i]
                    except IndexError:
                        val = ''
                    d.update({key: val})
                    i += 1
                dictlist.append(d)

            return dictlist
