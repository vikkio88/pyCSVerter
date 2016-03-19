from lib.config.validationrules import rules
from lib.config.validationrules import is_ascii
from lib.config.validationrules import config


class DataValidator(object):
    @staticmethod
    def validate(data_list):
        valid_rows = []
        for d in data_list:
            if DataValidator.is_valid(d):
                valid_rows.append(d)
        return valid_rows

    @staticmethod
    def is_valid(d):
        try:
            if config['discard_not_ascii']:
                for key in d:
                    if not is_ascii(str(d.get(key))):
                        raise Exception('Not valid String format')
            rules(d)
        except Exception as e:
            print("*******row discarded*********")
            print(e)
            print("*****************************")
            return False
        return True
