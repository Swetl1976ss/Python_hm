import pytest
from string_utils import StringUtils


utils = StringUtils()

def test_capitalize(): # позитивные тесты на строчную букву
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hi everyone") == "Hi everyone"
        assert utils.capitalize("") == ""

def trim(self, string: str) -> str:
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro   ") == "skypro"
    return string.lstrip()


def test_contains(): #Поиск нужного символа
        assert utils.contains("SkyPro", "S")
        assert not utils.contains("SkyPro", "U")  #негативные тест
        assert not utils.contains("", "A")   #негативные тест

def test_delete_symbol(): # Исключение заданного символа
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World!", "!") == "Hello World"
        assert utils.delete_symbol("", "x") == ""


#Негативные тесты

def test_capitalize_empty_string():
    result = utils.capitalize("")
    assert result == "", "Ожидается, что пустая строка останется пустой"
@pytest.mark.skip
def trim(self, string: str) -> str:
    if not isinstance(string, str):
        return None
    return string.lstrip()
@pytest.mark.skip
def test_contains_non_string_input():
    result = utils.contains(12345, "1")
    assert result is False