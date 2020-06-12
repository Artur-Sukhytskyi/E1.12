import random
from enum import Enum

def random_word(words):
	word = random.choice(words)
	return word

def user_letter(letter):
	if not letter.isalpha():
		raise ValueError

def insert_letter(hiden_word, letter, i):
	hiden_word = hiden_word[:i] + letter + hiden_word[i + 1:]
	return hiden_word

def open_letter(letter, word, hiden_word):
	for i, word_letter in enumerate(word):
		if word_letter == letter:
			hiden_word = insert_letter(hiden_word, letter, i)
	return hiden_word

def open_mistakes_count(mistakes_count):
	mistakes_count += 1
	return mistakes_count

def open_mistakes_text(mistakes_count):
	if mistakes_count == 1:
		mistakes_text = "Ошибка"
	else:
		mistakes_text = "Ошибки"
	return mistakes_text