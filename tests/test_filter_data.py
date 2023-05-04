import pytest

from utils import filter_data

# Положительный тест
def test_filter_data_1(test_data):
    data = filter_data(test_data)
    expected_data = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]
    assert expected_data == data


# Отрицательный тест
def test_det_filter_data():
    data = filter_data({})
    expected_data = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061', 'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501', 'to': 'Счет 43597928997568165086'}, {'id': 518707726, 'state': 'EXECUTED', 'date': '2018-11-29T07:18:23.941293', 'operationAmount': {'amount': '3348.98', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 3152479541115065', 'to': 'Visa Gold 9447344650495960'}, {'id': 649467725, 'state': 'EXECUTED', 'date': '2018-04-14T19:35:28.978265', 'operationAmount': {'amount': '96995.73', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 27248529432547658655', 'to': 'Счет 97584898735659638967'}, {'id': 782295999, 'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824', 'operationAmount': {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 24763316288121894080', 'to': 'Счет 96291777776753236930'}, {'id': 542678139, 'state': 'EXECUTED', 'date': '2018-10-14T22:27:25.205631', 'operationAmount': {'amount': '90582.51', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 2256483756542539', 'to': 'Счет 78808375133947439319'}]
    assert data == expected_data


