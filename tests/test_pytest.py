# import string, random

# import pytest

# import gallows_logic

# letters = string.ascii_lowercase
# hiden_letters = '_' * len(letters)
# letter = random.choice(letters)
# text = ["Ошибка", "Ошибки"]
# words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

# def test_open_letter():
# 	check_hiden_word = gallows_logic.open_letter(letter, letters, hiden_letters)
# 	assert check_hiden_word != hiden_letters

# def test_len_hiden_word():
# 	len_hiden_word = len(gallows_logic.open_letter(letter, letters, hiden_letters))
# 	assert len_hiden_word == len(hiden_letters)

# def test_random_word():
# 	word = gallows_logic.random_word(words)
# 	assert word in words

# def test_insert_letter():
# 	i = random.randint(0, len(hiden_letters))
#     check_hiden_word = gallows_logic.insert_letter(hiden_letters, letter, i)
#     assert check_hiden_word[i] == letter

# def test_open_mistakes_count():
# 	mistakes_count = random.randint(1, 10)
# 	opened_mistakes_count = gallows_logic.opened_mistakes_count(mistakes_count)
# 	assert opened_mistakes_count == mistakes_count + 1

# def test_open_mistakes_text():
# 	mistakes_count = random.randint(1, 10)
# 	mistakes_text = gallows_logic.opened_mistakes_text(mistakes_count)
# 	assert mistakes_text in text

import string, random

import pytest

import gallows_logic

letters = string.ascii_lowercase
hiden_letters = '_' * len(letters)
letter = random.choice(letters)
text = ['Ошибка', 'Ошибки']
words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

def test_open_letter():
    check_hiden_word = gallows_logic.open_letter(letter, letters, hiden_letters)
    assert check_hiden_word != hiden_letters

def test_len_hiden_word():
    len_hiden_word = len(gallows_logic.open_letter(letter, letters, hiden_letters))
    assert len_hiden_word == len(hiden_letters)

def test_random_word():
    word = gallows_logic.random_word(words)
    assert word in words

def test_insert_letter():
    i = random.randint(0, len(hiden_letters))
    check_hiden_word = gallows_logic.insert_letter(hiden_letters, letter, i)
    assert check_hiden_word[i] == letter

def test_open_mistakes_count():
    mistakes_count = random.randint(1, 10)
    opened_mistakes_count = gallows_logic.open_mistakes_count(mistakes_count)
    assert opened_mistakes_count == mistakes_count + 1

def test_open_mistakes_text():
    mistakes_count = random.randint(1, 5)
    mistakes_text = gallows_logic.open_mistakes_text(mistakes_count)
    assert mistakes_text in text