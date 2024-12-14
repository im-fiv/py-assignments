"""
Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.
"""

# определение функции суммации
def sum_series(n, m):
	sum = 0

	for num in range(n, m + 1):
		sum += num
	
	return sum

# запрашивание чисел
try:
	n = int(input('n = '))
	m = int(input('m = '))

	print(f'Сумма чисел от n до m = {sum_series(n, m)}')
except ValueError:
	print('Значения введены неверно!')