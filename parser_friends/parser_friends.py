import vk_api
import re
import pandas as pd
from tqdm import tqdm
from datetime import datetime


class ParserFriends:
    """
    Класс представляет возможность получить спиок друзей из соц. сети Vk в формате .csv

    ...

    Атрибуты
    --------
    token : str
        Авторизационный токен

    Методы
    ------
    get_friends():
        Возвращает словарь с данными пользователей Vk
    convert_birth_day():
        Конвертирует день рождение пользователя в ISO формат
    """
    def __init__(self, token: str) -> None:
        self.session = vk_api.VkApi(token=token)


    def __call__(self, user_id: int, path_to_save: str, extension_file: str='csv') -> None:
        '''
        Записывает данные пользователей в .csv формат

                Параметры:
                        user_id (int): ID пользователя
                        path_to_save (str): Путь к выходному файлу
                        extension_file (str): Формат выходного файла

                Возвращаемое значение:
                        None
        '''
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
                bdate = self.convert_birth_day(bdate)
            except KeyError:
                bdate = "NULL"

            sex = friends['items'][i]['sex']

            if sex == 1:
                sex = 'женский'
            elif sex == 2:
                sex = 'мужской'
            else:
                sex = 'не указано'

            result_dict[i] = {'first_name': first_name, 
                              'last_name': last_name, 
                              'country': country, 
                              'city': city, 
                              'bdate': bdate, 
                              'sex': sex}

        if extension_file == 'csv':
            path_to_save = f'{path_to_save}.csv'

            df = pd.DataFrame.from_dict(result_dict, orient='index')
            df.sort_values('first_name', inplace=True)
            df.to_csv(path_to_save, index=False)

    
    def get_friends(self, user_id: int) -> dict:
        '''
        Возвращает словарь с данными пользователей Vk.

                Параметры:
                        user_id (int): ID пользователя

                Возвращаемое значение:
                        return (dict): словарь с данными пользователя Vk 
        '''
        return self.session.method('friends.get', {'user_id': user_id, 'fields': 'country, bdate, city, sex'})

    def convert_birth_day(self, b_day: str) -> str:
        '''
        Возвращает дату рождения в ISO формате.

                Параметры:
                        b_day (str): дата рождения в формате dd.mm или dd.mm.yy

                Возвращаемое значение:
                        date (str): дата рождения в ISO формате.
        '''
        r = len(re.findall(r'[.]', b_day))
        
        if r == 2:
            date = datetime.strptime(b_day, '%d.%m.%Y')
            date.isoformat()
            date = str(date)[:10]
        else:
            date = datetime.strptime(b_day, '%d.%m')
            date.isoformat()
            date = str(date)[5:10]

        return date
