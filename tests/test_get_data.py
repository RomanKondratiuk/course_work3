import pytest
import json

from utils import get_data

# Положительный тест
def test_get_data_1(test_data):
    file = 'operations.json'
    expected_file = 'operations.json'
    assert file == expected_file




# Отрицательный тест
def test_get_data_2(test_data):
    file = 'operations.json_2'
    expected_file = 'operations.json'
    assert file == expected_file


