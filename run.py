import os
import argparse
from parser_friends import ParserFriends


parser = argparse.ArgumentParser()

parser.add_argument('--token', help='Your authorized token', type=str)
parser.add_argument('--user_id', help='User ID for which the report is being generated', type=int)
parser.add_argument('--file_extension', help='Output file format', nargs='?', type=str, default='csv')
parser.add_argument('--path_to_save', help='Path to the output file', nargs='?',
                    type=str, default=f'{os.getcwd()}/report')

args = parser.parse_args()


if __name__ == '__main__':
    print('Connecting to vk_api...')
    parse_data = ParserFriends(args.token, args.file_extension)
    parse_data(args.user_id, args.path_to_save)
