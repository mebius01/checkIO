#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

Вх. данные: Текст для анализа, как строка (str, unicode).

Вых. данные: Наиболее частая буква, как строка.

Примеры:

checkio("Hello World!") == "l"

checkio("How do you do?") == "o"

checkio("One") == "e"

checkio("Oops!") == "o"

checkio("AAaooo!!!!") == "a"

checkio("abe") == "a"

Как это используется: Для большинства задач по дешифрованию необходимо знать частоту появления различных букв в подобном тексте. Для примера, мы легко можем взломать одноалфавитный шифр подстановки, если мы знаем вероятность появления букв. Это также может быть полезной информацией для лингвистов.

Предусловия:
text содержит только ASCII символы.
0 < len(text) ≤ 105 
"""

def checkio(text):
	text=text.lower(); l={}
	for i in text:
		if i.isalpha():
			if i in l.keys():
				l[i]=l.get(i)+1
			elif i not in l.keys():
				l[i]=1
	sort_key=l.keys(); sort_key.sort()
	if sum(l.values()) == len(l):
		return sort_key[0]
	else:
		index_v=l.values().index(max(l.values()))
		return l.keys()[index_v]
	#~ return sort_key, l.keys()
	#replace this for solution


	#These "asserts" using only for self-checking and not necessary for auto-testing
print  checkio(u"Hello World!") == "l", "Hello test"
print  checkio(u"How do you do?") == "o", "O is most wanted"
print  checkio(u"One") == "e", "All letter only once."
print  checkio(u"Oops!") == "o", "Don't forget about lower case."
print  checkio(u"AAaooo!!!!") == "a", "Only letters."
print  checkio(u"abe") == "a", "The First."
print  checkio(u"fsbd") == "b" 
	#~ print("Start the long test")
print  checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
	#~ print("The local tests are done.")
''' "fsbd" '''

