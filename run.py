 # 248042549
# vk1.a.ashTijvMSvw7z6fj166-xrMOWbX4pJoZjbxyH04sL_ZIv0aU4wspsq-7nlo5blF-XEwins3_WXPN6NqagH9OQWBvzNha9TbTeZWuvkX6e4BzqIcCUxcJKoX8iwPJ3w0CLCSnDmpA3fZeQwU4b5Q6-FRGzc_MTbXkr1f9Tpt0HVXHk0Y5xps1MPpRZVVNQs5e
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