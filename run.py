import os
import argparse
from parser_friends import ParserFriends


parser = argparse.ArgumentParser()

parser.add_argument('token', help='Your authorized token')
parser.add_argument('user_id', help='User ID for which the report is being generated')
parser.add_argument('file_extension', help='Output file format', nargs='?', default='csv')
parser.add_argument('path_to_save', help='Path to the output file', nargs='?', default=f'{os.getcwd()}/report')

args = parser.parse_args() 


if __name__ == '__main__':
    parse_data = ParserFriends(args.token)
    parse_data(args.user_id, args.path_to_save)