import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def get_list_of_pets(self, url: str, token: str, path: str, filter: str):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком всех питомцев на платформе. В случае использования в запросе единственного доступного фильтра
        'my_pets' - сервер возвращает список только тех питомцев, которые были добавлены лично пользователем."""

        headers = {'auth_key': token}
        filter = {'filter': filter}
        res = requests.get(url + path, headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, url: str, path: str, token: str, name: str, breed: str, age: str, photo: str):
        """Метод посредством POST запроса отправляет на сервер полные данные о добавляемом питомце, включая фото,
        а также возвращает статус запроса на сервер (код состояния ответа) и результат в формате JSON с данными
        добавленного питомца."""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': breed,
                'age': age,
                'pet_photo': (open(photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': token, 'Content-Type': data.content_type}
        res = requests.post(url + path, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result

    def create_pet_simple(self, url, path, auth_key, name, animal_type, age):
        """Метод отправляет на сервер базовую информацию о добавляемом питомце без фотографии.
        Возвращает код состояния ответа на запрос и данные добавленного питомца в формате JSON."""

        headers = {'auth_key': auth_key}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.post(url + path, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
