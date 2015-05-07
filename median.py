#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Медиана - это числовое значение, которое делит сортированый массив чисел на большую и меньшую половины.
В сортированом массиве с нечетным числом элементов медиана - это число в середине массива.
Для массива с четным числом элементов, где нет одного элемента точно посередине, медиана - это среднее значение двух чисел,
находящихся в середине массива. В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.

Входные данные: Массив как список (list) чисел (int).

Выходные данные: Медиана как число (int, float).

Предусловия:
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data) 
"""
#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
	data.sort()
	if len(data)%2 == 1:
		return data[len(data)/2]
	elif len(data)%2 == 0:
		a=(len(data)/2)
		b=(len(data)/2)-1
		return (data[a]+data[b])/2.0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
	assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
	assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
	assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
	print("Start the long test")
	assert checkio(range(1000000)) == 499999.5, "Long."
	print("The local tests are done.")
