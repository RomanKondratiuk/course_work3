import json
from datetime import datetime


def get_data():
    """Функция для получения данных из файла"""

    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    """Функция для фильтрации транзакций"""

    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    """Подфункция"""
    return x['date']


def sort_data(data):
    """Функция для сортировки транзакций"""

    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def format_data(data):
    """Функция для форматирования даты и валюты"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        # получатель и отправитель
        description = row['description']
        recipient = row['to']
        new_recipient = f"{recipient[:4]} **{recipient[-4:]}"
        # Валюта
        amount = row['operationAmount']
        new_amount = amount['amount']
        currency_1 = row['operationAmount']
        currency = currency_1['currency']
        new_currency = currency['name']
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()  # делим по пробелам
            sender_bill = sender.pop(-1)  # pop удаляет последний элемент из списка
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]} ** **** {sender_bill[-4:]}"
        else:
            sender_info = "Новый счет ->"
            sender_bill = ""
            from_arrow = ""

        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {new_recipient}
{new_amount} {new_currency}
           """)
    return formatted_data


