import os
from parser_friends import ParserFriends

path = os.getcwd()

if __name__ == '__main__':
    token = 'vk1.a.dtU4jnh2_9diKVlPON44jfERpyncUYGyRk0T52CG5hlwbSkb9X1tpl8rqEP4xxJZh23xGs8Xq_9HRAayg8AgkvIANw0zC4c6tZWR-eTp2cYSNOhbh5I7DQy6YOwltlEqHFaAM_tsQwAfM81BHwzZOWjrtHFFQIE0_2Hp0-b3Ue02E7dbHHEfbIV0o5V_XCAz'
    user_id = 248042549
    
    parse_data = ParserFriends(token)
    parse_data(user_id, f'{path}/ivan_guy.csv')