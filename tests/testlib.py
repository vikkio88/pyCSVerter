import unittest
from lib.helpers.datavalidator import DataValidator
from lib.helpers.outputdumper import OutputDumper

"""Examples of how I would have structured UnitTests, if I had more time"""


class TestGameLibs(unittest.TestCase):
    def test_data_validator(self):
        invalid_dict = {"name": None}
        valid_dict = {"address": "63847 Lowe Knoll, East Maxine, WA 97030-4876", "contact": "Dr. Sinda Wyman",
                      "name": "The Gibson", "phone": "1-270-665-9933x1626",
                      "stars": 5}
        self.assertFalse(DataValidator.is_valid(invalid_dict))
        self.assertTrue(DataValidator.is_valid(valid_dict))

    def test_output_dumper(self):
        invalid_output_format = 'jpeg'
        self.assertRaises(Exception, OutputDumper.dump, [{}], invalid_output_format, 'dummy.' + invalid_output_format)


if __name__ == '__main__':
    unittest.main()
