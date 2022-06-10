import unittest
from parser_friends import ParserFriends


class TestParserFriends(unittest.TestCase):

    def setUp(self):
        self.parse_friends = ParserFriends(token='')

    def test_convert_birthday(self,):
        convert1 = self.parse_friends.convert_birth_day('20.01')
        convert2 = self.parse_friends.convert_birth_day('20.01.2000')

        self.assertEqual(str(type(convert1)), "<class 'str'>")
        self.assertEqual(str(type(convert2)), "<class 'str'>")


if __name__ == '__main__':
    unittest.main()
