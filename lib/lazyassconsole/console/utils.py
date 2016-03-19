from .console import Console


class Utils(object):
    @staticmethod
    def choose_one_from_list(target_list):
        index = input("({}/{}) > ".format(1, len(target_list)))
        index = int(index)
        index -= 1
        while index < 0 or index >= len(target_list):
            Console.print("wrong choice, try again", 'r')
            index = input("({}/{}) > ".format(1, len(target_list)))
            index = int(index)
            index -= 1
        return target_list[index]
