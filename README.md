# VK get friends

Данная система позволяет получить список друзей из Вконтакте

## Инструкция по пользованию

Для запуска потребуется командная строка. Первым делом нужно установить необходимые зависимости:
```bash 
pip install -r requirements.txt
```

Программа принимает на вход 4 аргумента:

* token - авторизационный токен (инструкция для его получения чуть ниже)
* user_id - ID пользователя, для которого генерируем отчет (Если ID задан в символьном виде, конвертировать его тут [regvk](https://regvk.com/id/))
* file_extension (optional) - Формат выходного файла (CSV, JSON, TSV)
* path_to_save (optional) - Путь к выходному файлу (по умолчанию - файл с именем report в текущей директории)

Пример:
```bash 
python -m run --token {ваш токен} --user_id {ID пользователя} --file_extension {формат выходного файла} --path_to_save {путь к выходному файлу}
```
## Получение access token
1. Перейдите по этой ссылке [vkhost.github.io](https://vkhost.github.io/)
2. Нажмите на вкладку настройки, там выберите "Друзья" и "Доступ в любое время"
3. Затем нажмите "разрешить"
4. Скопируйте часть адресной строки от _access_token=_ до _&expires_in_

## Как работает скрипт
* Для взаимодействия с командной строкой используется _argspace_ - модуль для обработки аргументов командной строки.
* Чтобы получить списко друзей используется [_vk_api_](https://dev.vk.com/reference)

Для работы со всеми методами API вам необходимо передавать в запросе [_access_token_](https://dev.vk.com/api/access-token/getting-started) — специальный ключ доступа.
Этот скрипт использует только один метод - это [friends.get](https://dev.vk.com/method/friends.get), который возвращает список ID друзей и расширенную информацию
о друзьях пользователя.
