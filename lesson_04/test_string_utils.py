import pytest
from string_utils import StringUtils

def test_string_utils_capitalized(): #Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
    assert StringUtils.capitalize("skypro")=="Skypro"

def test_string_utils_trim():#Принимает на вход текст и удаляет пробелы в начале, если они есть
    assert StringUtils.trim("   skypro")=="skypro"

def test_string_utils_contains():# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
    assert StringUtils.contains("SkyPro", "S") is True
    assert StringUtils.contains("SkyPro", "U") is False  # запомнить True и False в Pythonпишутся без ковычек

def test_string_utils_delete_symbol():# Удаляет все подстроки из переданной строки
   
    assert StringUtils.delete_symbol("SkyPro", "k") == "SyPro"
    assert StringUtils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_string_utils_positive_format(): #Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
    assert StringUtils.format("Test")=="Test"

def test_string_utils_isnumeric_negative_digits(): #Принимает на вход числа,  и возвращает эти же числа
    assert StringUtils.isnumeric_positive_digits("12345O") is True

def test_string_utils_isnumeric_negative_minus(): #отрицательные числа не проходят из-за знака минус
    assert StringUtils.isnumeric_positive_digits("-10") is False

def test_string_utils_isnumeric_negative_empty(): # пустая строка всегда False
    assert StringUtils.isnumeric_positive_digits("") is False

def test_string_utils_isnumeric_negative_letters(): # пустая строка с пробелом всегда False
    assert StringUtils.isnumeric_positive_digits(" ") is False

def test_string_utils_isnumeric_positive_format_with_spaces(): #  строка с пробелами всегда True
    assert StringUtils.isnumeric_positive_digits("04 апреля 2023") is True

def test_string_utils_isnumeric_negative_none(): #  None всегда false
    assert StringUtils.isnumeric_positive_digits(None) is False
