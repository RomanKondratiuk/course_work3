import pytest

from utils import sort_data

# Положительный тест
def test_sort_data_1(test_data):
    expected_value = sort_data(test_data)
    assert [x['date'] for x in expected_value] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']




# Отрицательный тест
def test_sort_data_2(test_data):
    expected_value = sort_data(test_data)
    assert [x['date'] for x in expected_value] == ['2022-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                                                       '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']
