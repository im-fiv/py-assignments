"""
Единицы массы пронумерованы следующим образом:
1 - килограмм,
2 - миллиграмм,
3 - грамм,
4 - тонна,
5 - центнер.
Дан номер единицы массы (целое число в диапазоне 1-5) и масса тела в этих единицах (вещественное число).
Найти массу тела в килограммах.
"""

try:
	# принимаем номер единицы массы из ввода пользователя
	unit = int(input('Введите номер единицы массы: '))

	# принимаем количество данной единицы массы из ввода пользователя
	amount = float(input('Введите количество выбранной единицы массы: '))

	kg_ratios = {
		# 1 КГ = 1 КГ
		1: (1, 'КГ'),
		# 1 мГ = 1/1000000 КГ
		2: (1/1_000_000, 'мГ'),
		# 1 Г = 1/1000 КГ
		3: (1/1_000, 'Г'),
		# 1 Т = 1000 КГ
		4: (1_000, 'Т'),
		# 1 ц = 100 КГ
		5: (100, 'ц')
	}

	# получаем соотношение к килограммам
	ratio = kg_ratios[unit]
	# умножаем
	converted_amount = amount * ratio[0]

	# выводим с единицами
	print(f'{amount} {ratio[1]} = {converted_amount} КГ')
except ValueError:
	print('Значения введены неверно!')