# Нужно написать программу, которая принимает на вход
# путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;

import requests

# Путь к файлу на компьютере
file_path = 'ПУТЬ'

# URL для загрузки файла на Яндекс.Диск
upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

# Параметры запроса
params = {'path': 'ИМЯ', 'overwrite': 'true'}

# Заголовки запроса
headers = {'Authorization': 'ТОКЕН'}

# Отправляем запрос на получение ссылки для загрузки файла
response = requests.get(upload_url, params=params, headers=headers)

# Обрабатываем JSON-ответ
json_response = response.json()
href = json_response['href']

# Открываем файл для чтения байтов
with open(file_path, 'rb') as file:
    # Отправляем запрос методом PUT для загрузки файла на Яндекс.Диск
    upload_response = requests.put(href, data=file, headers=headers)

# Проверяем статус-код ответа
if upload_response.status_code == 201:
    print('Файл успешно загружен на Яндекс.Диск')
else:
    print(f'Не удалось загрузить файл на Яндекс.')