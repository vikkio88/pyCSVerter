class IFormatter(object):
    input_dict = {}
    output_format = None

    def str_dump(self, dictionary, filename): raise NotImplementedError
