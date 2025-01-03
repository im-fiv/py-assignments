"""
Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K
справа цифру D
(D - входной параметр целого типа, лежащий в диапазоне 0-9,
K - параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2,
выводя результат каждого добавления
"""

def AddRightDigit(D, K):
	# поскольку `K` не может превышать число 9,
	# чтобы добавить цифру справа, достаточно сместить число на 1 разряд влево
	# и сложить с `D`
	return K * 10 + D

try:
	# получаем целое число от пользователя
	K = int(input('K = '))

	# добавляем цифру 1 и выводим результат
	K = AddRightDigit(1, K)
	print(f'{K = }')

	# добавляем цифру 2 и выводим результат
	K = AddRightDigit(2, K)
	print(f'{K = }')
except ValueError:
	print('Значения введены неверно!')