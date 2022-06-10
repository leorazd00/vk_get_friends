import vk_api
import os
import pandas as pd
from tqdm import tqdm


class ParserFriends:
    def __init__(self, token: str) -> None:
        self.session = vk_api.VkApi(token=token)


    def __call__(self, user_id: int, path_to_save: str, extension_file: str='csv') -> None:
        friends = self.get_friends(user_id)
        

        result_dict = {}
        for i in tqdm(range(len(friends['items']))):
            first_name = friends['items'][i]['first_name']
            last_name = friends['items'][i]['last_name']

            try:
                country = friends['items'][i]['country']['title']
            except KeyError:
                country = "NULL"
            
            try:
                city = friends['items'][i]['city']['title']
            except KeyError:
                city = "NULL"

            try:
                bdate = friends['items'][i]['bdate']
            except KeyError:
                bdate = "NULL"

            sex = friends['items'][i]['sex']

            if sex == 1:
                sex = 'женский'
            elif sex == 2:
                sex = 'мужской'
            else:
                sex == 'не указано'

            dict_info = {'first_name': first_name, 
                        'last_name': last_name, 
                        'country': country, 
                        'city': city, 
                        'bdate': bdate, 
                        'sex': sex}

            result_dict[i] = dict_info

        if extension_file == 'csv':
            path_to_save = f'{path_to_save}.csv'

            df = pd.DataFrame.from_dict(result_dict, orient='index')
            df.to_csv(path_to_save, index=False)

    
    def get_friends(self, user_id: int) -> dict:
        return self.session.method('friends.get', {'user_id': user_id, 'fields': 'country, bdate, city, sex'})