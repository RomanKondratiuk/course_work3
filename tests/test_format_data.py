import pytest

from utils import format_data

# Положительный тест
def test_format_data_1(test_data):
    data = format_data(test_data)
    expected_data_value = ['\n26.08.2019 Перевод организации\nMaestro 1596 83 ** **** 5199 -> Счет **9589\n31957.58 руб.\n           ', '\n03.07.2019 Перевод организации\nMasterCard 7158 30 ** **** 6758 -> Счет **5560\n8221.37 USD\n           ', '\n30.06.2018 Перевод организации\nСчет 7510 68 ** **** 6952 -> Счет **6702\n9824.07 USD\n           ', '\n23.03.2018 Открытие вклада\nНовый счет ->   Счет **2431\n48223.05 руб.\n           ']
    assert data == expected_data_value





# Отрицательный тест
def test_format_data_2(test_data):
    data = format_data(test_data)
    expected_data_value = ['\n30.08.2019 Перевод организации\nMaestro 1596 83 ** **** 5199 ->\\     \n           ', '\n03.07.2019 Перевод организации\nMasterCard 7158 30 ** **** 6758 ->\\     \n           ', '\n30.06.2018 Перевод организации\nСчет 7510 68 ** **** 6952 ->\\     \n           ', '\n23.03.2018 Открытие вклада\nНовый счет  \\     \n           ']
    assert data == expected_data_value


