import os
from parser_friends import ParserFriends

path = os.getcwd()

if __name__ == '__main__':
    token = ''
    user_id = 248042549

    parse_data = ParserFriends(token)
    parse_data(user_id, f'{path}/ivan_guy.csv')