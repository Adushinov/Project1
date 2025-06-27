<div id="header" align="center">
  <img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHNoMDlwa25vdmZlOGwxZDV6OHpkZHE5a3JnczU0ejMzaGR5enoxeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/78XCFBGOlS6keY1Bil/giphy.gif width="200"/>
</div>

## :computer: Коротко о моем проекте:
Данный проект связан с домашней работой курса от SkyPro, в нем IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 

---

### 
<h1>
Установка
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXQ3azJyMDB4aTI3emc1eHJndzYwbmoxeDVqdXE4YXM4bmVsYWxvOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/HhuPdJhvE05fclU5s5/giphy.gif" width="50px"/>
</h1>

1. Клонируйте репозиторий:
```
git@github.com:Adushinov/Project1.git
```

2. Установите зависимости:
```
poetry install
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```

5. Активировать окружение:
```
poetry shell
```

## 
<h1>
Использование:
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzhsY3lvamhmaTIxa2hsN2MzeGRuNDR5ZmR1cjU0dWV5d3ZwM2loNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HzPtbOKyBoBFsK4hyc/giphy.gif"
width="50px"/>
</h1>
    
1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

---

###
<h1>
Пример использования функций:
  <img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2syeGFlMWlzb3J2eTM0ZnR0dzcweGJianEyYmo3NG41eWg5ZHM0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u1WhXLjwgcXpHJBMRM/giphy.gif'
width='70px'/>
</h1>

1. Функция get_mask_card_number:
```
 7000792289606361     # входной аргумент
 7000 79** **** 6361  # выход функции
 ```
                               
2. Функция get_mask_account:
```
73654108430135874305  # входной аргумент
**4305  # выход функции
```
3. Функция mask_account_card:
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
4. Функция get_date:
```
print(get_date("2025-06-14T12:00:00"))  # Вывод: 14.06.2025
```
5. Функция filter_by_state:
```
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
6. Функция sort_by_date:
```
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
7. Функция filter_by_cerrency
```
if __name__ == "__main__":
    # Пример списка транзакций
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                },
                "amount": 100.0
            },
            "description": "Покупка в магазине"
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                },
                "amount": 80.0
            },
            "description": "Перевод средств"
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                },
                "amount": 150.0
            },
            "description": "Оплата услуги"
        }
    ]

    # Фильтрация транзакций по валюте USD
    filtered_transactions = filter_by_currency(transactions, "USD")

    # Вывод отфильтрованных транзакций
    for transaction in filtered_transactions:
        print(transaction)
```
8. Генератор transaction_descriptions
```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
9. Генератор card_number_generator
```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
---

<h1>
Тестирование:
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTI4c3hqcThraHB5aWJqM2JhNTNheWk0cXh1NG0wamtyaWh1dGcyeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Ll22OhMLAlVDb8UQWe/giphy.gif"
width="70px"/>
</h1>

1. Установите pytest:
```
poetry add --group dev pytest
```
2. Запустить тесты с оценкой покрытия:
```
poetry run rytest --cov
```
3. Сгенерируйте отчет о тестирование: 
```
coverage html
```
4. Ознакомьтесь с подробным отчетом о тестировании:
```
htmlcov/index.html
```
