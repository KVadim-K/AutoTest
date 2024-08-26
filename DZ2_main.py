import pytest
from DZ2 import count_vowels

def test_all_vowels():  # Проверяет, что функция корректно считает количество гласных в строках, содержащих только гласные.
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():  # Проверяет, что функция возвращает 0 для строк, не содержащих гласных.
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0

def test_mixed_string():  # Проверяет, что функция корректно считает количество гласных в строках, содержащих гласные и согласные.
    assert count_vowels("Hello World") == 3
    assert count_vowels("PyTest is FUN") == 3
    assert count_vowels("123456") == 0
    assert count_vowels("Python3.9") == 1