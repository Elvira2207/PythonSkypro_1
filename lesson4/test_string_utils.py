import pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [("hello", "Hello")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize('input_str, expected', [("  Hello", "Hello")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize('input_str, symbol, expected', [("Hello", "He", True)])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.parametrize('input_str, symbol, expected', [("Hello", "H", "ello")])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [("", ""), ("123", "123")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize('input_str, expected', [(" ", "")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize('input_str, symbol, expected', [("Hello", "R", False)])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.parametrize('input_str, symbol, expected', [("Hello", "R", False)])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

