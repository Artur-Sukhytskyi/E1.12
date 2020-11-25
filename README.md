# Using-travis-ci

[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/Artur-Sukhytskyi/E1.12/master.png?style=flat-square

[build]: https://travis-ci.org/Artur-Sukhytskyi/E1.12

Написать приложение, создать к нему pull request на github, написать тесты, посчитать покрытие ими кода и настроить непрерывную интеграцию с travis-ci.

ТЗ:
Реализовывать игру в виселицу. Приложение «загадывает» одно из следующих слов: skillfactory, testing, blackbox, pytest, unittest, coverage. И показывает количество букв в нём.
  Игрок пытается угадать слово буква за буквой. Если человек называет букву, которой нет в слове, у него появляется штрафное очко. А если букву, которая есть в слове, то она открывается (и все её вхождения).
  Например, было загадано слово testing. На первом ходу игроку показывают: _ _ _ _ _ _ _.
  Допустим, пользователь предположил, что в этом слове есть буква a. Изображение слова остаётся такое же: _ _ _ _ _ _ _, но у пользователя появляется штрафное очко.
  Допустим, на следующем ходу пользователь предлагает букву t. Тогда изображение слова меняется, игроку открывается буква t: T _ _ T _ _ _.
  Если набирается 4 штрафных очка и слово не отгадано, игра проиграна.
  Приложение должно управляться через командную строку.

Write an application, create a pull request for it on github, write tests, calculate their code coverage and set up continuous integration with travis-ci.

TT:
Implement the gallows game. The application makes one of the following words: skillfactory, testing, blackbox, pytest, unittest, coverage. And it shows the number of letters in it.
  The player tries to guess the word letter by letter. If a person names a letter that is not in the word, he has a penalty point. And if the letter that is in the word, then it opens (and all its occurrences).
  For example, the word testing was coded. On the first move, the player is shown: _ _ _ _ _ _ _.
  Let's say the user guesses that this word contains the letter a. The image of the word remains the same: _ _ _ _ _ _ _, but the user gets a penalty point.
  Let's say on the next move the user offers the letter t. Then the image of the word changes, the player opens the letter t: T _ _ T _ _ _.
  If 4 penalty points are scored and the word is not guessed, the game is lost.
  The application must be controlled via the command line.
