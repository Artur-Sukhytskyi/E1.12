import random
from enum import Enum

from gallows_logic import random_word, user_letter, open_letter, open_mistakes_count, open_mistakes_text

words = ["skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage"]
word = random_word(words)
mistakes = 3

print("Добро пожаловать на игру 'Висилеца'")
print("Угадайте слово из {} букв. Слово на английском языке".format(len(word)))
print("У вас есть {} попытки".format(mistakes + 1))

hiden_word = "_" * len(word)
mistakes_count = 0;
endgame_print = "Вы отгадали слово {}".format(word)

while "_" in hiden_word:

	print(hiden_word)
	print("Введите букву")
	letter = input()
	try:
		user_letter(letter)
	except ValueError:
		print("Используйте буквы")
	if letter in word:
		hiden_word = open_letter(letter, word, hiden_word)
	else:
		mistakes_count = open_mistakes_count(mistakes_count)
		mistakes_text = open_mistakes_text(mistakes_count)
		print("{} {}".format(mistakes_count, mistakes_text))
	if mistakes_count > mistakes:
		endgame_print = "{} ошибки. Вы проиграли".format(mistakes_count)
		break
# if(mistakes_count < mistakes):
# 	print(hiden_word)
print(endgame_print)