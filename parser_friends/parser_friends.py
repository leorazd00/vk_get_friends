import vk_api
import re
import json
import pandas as pd
from tqdm import tqdm
from datetime import datetime

good_extension = ['csv', 'json', 'tsv']


class ParserFriends:
    """
    Класс представляет возможность получить список друзей
    из соц. сети Vk в формате csv, json, tsv.
    """

    def __init__(self, token: str,
                 user_id: int,
                 extension_file: str = 'csv') -> None:
        '''
        Инициализирует необходимые переменные.

                Параметры:
                        token (str): Авторизационный токен
                        user_id (int): ID пользователя
                        extension_file (str): Формат выходного файла

                Возвращаемое значение:
                        None
        '''
        self.session = vk_api.VkApi(token=token)
        self.user_id = user_id
        self.extension_file = extension_file

        assert self.extension_file in good_extension, \
               f'Доступные форматы для выходного файла: {good_extension}'

    def __call__(self, path_to_save: str) -> None:
        '''
        Записывает данные пользователей в одном из доступных форматов

                Параметры:
                        path_to_save (str): Путь к выходному файлу

                Возвращаемое значение:
                        None
        '''
        friends = self.get_friends(self.user_id)

        result_dict = {}
        for i in tqdm(range(len(friends)), desc='Progress'):
            first_name = friends[i]['first_name']
            last_name = friends[i]['last_name']

            try:
                country = friends[i]['country']['title']
            except KeyError:
                country = "NULL"
            try:
                city = friends[i]['city']['title']
            except KeyError:
                city = "NULL"

            try:
                bdate = friends[i]['bdate']
                bdate = self.convert_birth_day(bdate)
            except KeyError:
                bdate = "NULL"

            sex = friends[i]['sex']

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

        self.write_to_file(result_dict, path_to_save)

    def get_friends(self, user_id: int) -> list:
        '''
        Возвращает список словарей с данными пользователей Vk.

                Параметры:
                        user_id (int): ID пользователя

                Возвращаемое значение:
                        return (list): список со словарями,
                                       данных пользователей Vk
        '''
        dict_args = {'user_id': user_id, 'fields': 'country, bdate, city, sex'}
        req1 = self.session.method('friends.get', dict_args)['items']

        if len(req1) == 5000:
            dict_args['offset'] = 5000
            req2 = self.session.method('friends.get', dict_args)['items']
            return req1 + req2

        return req1

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
            try:
                date = datetime.strptime(b_day, '%d.%m.%Y')
                date.isoformat()
                date = str(date)[:10]
            except ValueError:
                # Высокосный год
                year = b_day[:-5:-1]
                date = f'{year}-29-02'
        else:
            try:
                date = datetime.strptime(b_day, '%d.%m')
                date.isoformat()
                date = str(date)[5:10]
            except ValueError:
                # Высокосный год
                date = '29-02'

        return date

    def write_to_file(self, data: dict, path_to_save: str) -> None:
        '''
        Записывет информацию о пользователях в нужный формат.

                Параметры:
                        data (dict): словарь с инф. о пользователях
                        path_to_save (str): путь для сохранения файла

                Возвращаемое значение:
                        None
        '''
        if self.extension_file == 'csv':
            path_to_save = f'{path_to_save}.csv'

            df = pd.DataFrame.from_dict(data, orient='index')
            df.sort_values('first_name', inplace=True)
            df.to_csv(path_to_save, index=False)
        elif self.extension_file == 'json':
            path_to_save = f'{path_to_save}.json'
            sorted_dict = dict(sorted(data.items(),
                               key=lambda x: x[1].get('first_name')))

            with open(path_to_save, 'w', encoding='utf-8') as outfile:
                json.dump(sorted_dict, outfile, ensure_ascii=False, indent=4)
        else:
            path_to_save = f'{path_to_save}.tsv'

            df = pd.DataFrame.from_dict(data, orient='index')
            df.sort_values('first_name', inplace=True)
            df.to_csv(path_to_save, sep='\t', index=False)
