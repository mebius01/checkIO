#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из
неуникальных элементов данного массива. Для этого необходимо удалить все уникальные элементы (которые присутствуют
в данном массиве только один раз). Для решения этой задачи не меняйте оригинальный порядок элементов.
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].

non-unique-elements

Вх. данные: Список (list) целых чисел (int).

Вых. данные: Список (list) целых чисел (int).

Пример:

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]

checkio([1, 2, 3, 4, 5]) == []

checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

Как это используется: Эта задача поможет вам понять, как манипулировать массивами.
Это полезный базис для решения более сложных задач. Также эта идея может быть легко обобщена для реальных задач.
Для примера: если вам необходимо очистить статистику от редко встречающихся элементов (шум).
"""
#Your optional code here
#You can import some modules or create additional functions
def checkio(data):
	l=[]
	for i in data:
		if data.count(i) >= 2:
			l.append(i)
	return l
#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert isinstance(checkio([1]), list), "The result must be a list"
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
