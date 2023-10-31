## Стек технологий 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Flask](https://shields-io.translate.goog/badge/-Flask-464646?style=flat)](https://flask.palletsprojects.com/en/3.0.x/)



# Инструкция по запуску сервера



1. Склонируйте репозиторий на свою локальную машину.
2. Установите необходимые зависимости, указанные в requirements.txt, с помощью команды:
pip install -r requirements.txt


3. Запустите сервер с помощью команды:
python app.py



# Создание продукта

URL: /products
Метод: POST

Пример запроса:
{
"name": "Ноутбук",
"price": 1000.0
}



Пример успешного ответа:
{
"id": 1,
"name": "Ноутбук",
"price": 1000.0
}


# Получение всех продуктов

URL: /products
Метод: GET

Пример успешного ответа:
[
{
"id": 1,
"name": "Ноутбук",
"price": 1000.0
},
{
"id": 2,
"name": "Смартфон",
"price": 500.0
}
]



# Получение продукта по id

URL: /products/{id}
Метод: GET

Пример успешного ответа:
{
"id": 1,
"name": "Ноутбук",
"price": 1000.0
}


5. Запустите свой сервер с помощью функции run_server().


