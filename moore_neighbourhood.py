#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
В конечных автоматах, Окрестность Мура содержит восемь клеток, окружающие центральную ячейку двумерной квадратной решетки. Эта область названа в честь Эдварда Ф. Мура, пионера теории конечных автоматов. Существует множество настольных игр с прямоугольной сеткой квадратных ячеек. Для некоторых игр важно знать обстановку в соседних клетках для схемы размещения фишек и стратегии. 

 У вас имеется позиция для прямоугольного игрового поля, где 1 клетка с фишкой, а 0 пустая. Также есть координатная сетка, в форме строк и столбцов (нумерация с 0). Вы должны определить сколько фишек близко к этой ячейке. Каждая клетка взаимодействует с восьмью соседними (Горизонтально, вертикально, по диагонали); 

 

 Для примера возьмем (см. рисунок) такую схему: 
((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)


 Для первого примера координаты ячейки (1, 2) и мы можем видеть на схеме, что у фишки есть 3 соседа. Для второго примера координаты ячейки (0, 0) и эта ячейка содержит фишку, но мы считаем только соседей поэтому ответ 1. 

Входные данные:  Три аргумента. Кортеж кортежей с числами (1/0), номер строки и колонки в виде целых чисел. 

Выходные данные:  Сколько соседей имеет клетка в виде целого числа. 


Предусловия:
 3 ≤ len(grid) ≤ 10
"""

def count_neighbours(grid, row, col):
	if (row == 0) and (col == 0): #(0,0)
		return grid[row][col+1]+grid[row+1][col+1]+grid[row+1][col]
	elif (row == 0) and ((col > 0) and (col < len(grid[0])-1)): #(0,1)
		return grid[row][col-1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1] + grid[row][col+1]
	elif (row == 0) and (col == len(grid[0])-1): #(0,5)
		return grid[row][col-1] + grid[row+1][col-1] + grid[row+1][col]

	elif ((row > 0) and row < len(grid[0])-1) and (col == 0): #(1,0)
		return grid[row-1][col] + grid[row-1][col+1] + grid[row][col+1] + grid[row+1][col+1] + grid[row+1][col]
	elif ((row > 0) and row < len(grid[0])-1) and ((col > 0) and (col < len(grid[0])-1)): #(1,1)
		return grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1] + grid[row][col-1] + grid[row][col+1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
	elif (row < len(grid[0])-1) and (col == len(grid[0])-1): #(1,5)
		return grid[row-1][col-1] + grid[row-1][col] + grid[row][col-1] + grid[row+1][col-1] + grid[row+1][col]

	elif (row == len(grid[0])-1) and (col == 0): #(5,0)
		return grid[row-1][col] + grid[row-1][col+1] + grid[row][col+1]
	elif (row == len(grid[0])-1) and ((col > 0) and (col < len(grid[0])-1)): #(5,1)
		return grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1] + grid[row][col-1] + grid[row][col+1]
	elif (row == len(grid)-1) and (col == len(grid[0])-1): #(5,5)
		return grid[row-1][col-1] + grid[row-1][col] + grid[row][col-1] 




#~ if __name__ == '__main__':
	#~ #These "asserts" using only for self-checking and not necessary for auto-testing
	#~ assert count_neighbours(
		#~ ((1, 0, 0, 1, 0),
		 #~ (0, 1, 0, 0, 0),
		 #~ (0, 0, 1, 0, 1),
		 #~ (1, 0, 0, 0, 0),
		 #~ (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
	#~ assert count_neighbours(((1, 0, 0, 1, 0),
							 #~ (0, 1, 0, 0, 0),
							 #~ (0, 0, 1, 0, 1),
							 #~ (1, 0, 0, 0, 0),
							 #~ (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
	#~ assert count_neighbours(((1, 1, 1),
							 #~ (1, 1, 1),
							 #~ (1, 1, 1),), 0, 2) == 3, "Dense corner"
	#~ assert count_neighbours(((0, 0, 0),
							 #~ (0, 1, 0),
							 #~ (0, 0, 0),), 1, 1) == 0, "Single"


print count_neighbours(
			((1,0,1,0,1),
			(0,1,0,1,0),
			(1,0,1,0,1),
			(0,1,0,1,0),
			(1,0,1,0,1),
			(0,1,0,1,0),), 5, 4)
