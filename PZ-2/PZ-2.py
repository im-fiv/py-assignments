"""
Дана масса M в килограммах.
Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).
"""

# Определяем переменную `M` и присваиваем ей значение `None`.
# Литерал `None` в Python позволяет представить `null` переменную, то есть переменную, которая не содержит какого-либо значения.
# Другими словами, `None` – это специальная константа, означающая пустоту. Если более точно, то `None` – это объект специального типа данных NoneType.
M = None

# Цикл `while` (`пока`) позволяет выполнить одну и ту же последовательность действий, пока проверяемое условие истинно.
# Условие записывается до тела цикла и проверяется до выполнения тела цикла.
# Как правило, цикл while используется, когда невозможно определить точное значение количества проходов исполнения цикла.
# В данном случае, мы сравниваем значения `type(M)` и строку `int`, и если они не равны, то выполняются действия,
# определённые внутри цикла.
#
# Метод `type()` в Python возвращает тип данных объекта.
# Он может быть использован для определения типа переменной или объекта во время выполнения программы.
# Строка `int` обозначает названия типа данных, который нам нужен.
while type(M) != 'int':
	# Исключения (exceptions) - ещё один тип данных в Python.
	# Исключения необходимы для того, чтобы сообщать программисту об ошибках.
	#
	# BaseException - базовое исключение, от которого берут начало все остальные.
	# 	SystemExit - исключение, порождаемое функцией `sys.exit` при выходе из программы.
	# 	KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
	# 	GeneratorExit - порождается при вызове метода close объекта generator.
	# 	Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
	# 	StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
	# 	ArithmeticError - арифметическая ошибка.
	# 	FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
	# 	OverflowError - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
	# 	ZeroDivisionError - деление на ноль.
	# 	AssertionError - выражение в функции `assert` ложно.
	# 	AttributeError - объект не имеет данного атрибута (значения или метода).
	# 	BufferError - операция, связанная с буфером, не может быть выполнена.
	# 	EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
	# 	ImportError - не удалось импортирование модуля или его атрибута.
	# 	LookupError - некорректный индекс или ключ.
	# 	IndexError - индекс не входит в диапазон элементов.
	# 	KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
	# 	MemoryError - недостаточно памяти.
	# 	NameError - не найдено переменной с таким именем.
	# 	UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
	# 	OSError - ошибка, связанная с системой.
	# 	BlockingIOError
	# 	ChildProcessError - неудача при операции с дочерним процессом.
	# 	ConnectionError - базовый класс для исключений, связанных с подключениями.
	# 	BrokenPipeError
	# 	ConnectionAbortedError
	# 	ConnectionRefusedError
	# 	ConnectionResetError
	# 	FileExistsError - попытка создания файла или директории, которая уже существует.
	# 	FileNotFoundError - файл или директория не существует.
	# 	InterruptedError - системный вызов прерван входящим сигналом.
	# 	IsADirectoryError - ожидался файл, но это директория.
	# 	NotADirectoryError - ожидалась директория, но это файл.
	# 	PermissionError - не хватает прав доступа.
	# 	ProcessLookupError - указанного процесса не существует.
	# 	TimeoutError - закончилось время ожидания.
	# 	ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
	# 	RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
	# 	NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
	# 	SyntaxError - синтаксическая ошибка.
	# 	IndentationError - неправильные отступы.
	# 	TabError - смешивание в отступах табуляции и пробелов.
	# 	SystemError - внутренняя ошибка.
	# 	TypeError - операция применена к объекту несоответствующего типа.
	# 	ValueError - функция получает аргумент правильного типа, но некорректного значения.
	# 	UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
	# 	UnicodeEncodeError - исключение, связанное с кодированием unicode.
	# 	UnicodeDecodeError - исключение, связанное с декодированием unicode.
	# 	UnicodeTranslateError - исключение, связанное с переводом unicode.
	# 	Warning - предупреждение.
	#
	# Теперь, зная, когда и при каких обстоятельствах могут возникнуть исключения, мы можем их обрабатывать. Для обработки исключений используется конструкция try - except.
	try:
		# Эта строка содержит сразу несколько действий в одном, давайте их рассмотрим по одному:
		# 1. Присвоение к переменной
		#		Переменная — это контейнер для хранения различных значений (данных).
		# 		Чтобы переменная получила какое-то значение, его нужно присвоить.
		#		В Python команда присвоить обозначается знаком `=` (`равно`),
		#		после него идет значение, которое нужно присвоить левому операнду данного действия.
		#
		# *Заметка: несмотря на то, что действия, которые мы не разобрали распологаются в следующем порядке:
		# 	`int()`, `input()`
		# Первым действием из данных двух будет выполнено `input()`
		#
		# 2. Вызов функции `input`
		#		2.1 Перед тем, как мы разберем, что такое `input`, мы должны понимать, что такое функция?
		#
		#			Функция в Python — это фрагмент кода, который выполняет определённые операции и отдаёт результат.
		#			Его можно написать один раз и переиспользовать во всей программе.
		#			В Python, как и в других языках программирования, есть особые правила для создания функций.
		#			Если их не соблюдать, то интерпретатор не сможет правильно обработать код и, скорее всего, выдаст ошибку.
		#		
		#			```
		#			def имя_функции(аргументы):
		#				тело_функции
		#				return результат
		#			```
		#
		#		2.2 Как вызвать функцию?
		#
		#			Функцию в Python можно создать один раз, а после вызывать её в коде неограниченное количество раз.
		# 			Это позволяет экономить время и сокращает количество строк в проекте.
		#
		#			Чтобы вызвать функцию, надо ввести её название и передать аргументы в скобках.
		# 			В общем виде синтаксис вызова выглядит так:
		#
		#			```
		#			имя_функции(аргументы)
		#			```
		#
		#			Теперь, после того как мы знаем, как вызывать функцию, можно поподробнее рассмотреть `input()`.
		#
		#
		#		2.3 Что такое функция `input()`?
		#
		#			В языке Python имеется встроенная функция `input()`, с помощью которой можно читать ввод пользователя.
		# 			Эта функция принимает необязательный строковый аргумент (который выводится в консоли как строка приглашения к вводу)
		# 			и ожидает, пока пользователь введет ответ и завершит ввод клавишей `Enter` (или `Return`).
		#
		#			Если пользователь не введет никакой текст и просто нажмет клавишу `Enter`,
		# 			функция `input()` вернет пустую строку, в противном случае она возвращает строку,
		# 			содержащую ввод пользователя без символа завершения строки.		
		#
		# 3. Что такое функция `int()`?
		#
		#		В языке программирования Python встроенная функция `int()` возвращает целое число (экземпляр класса `int`)
		# 		в десятичной системе счисления.
		# 		Если преобразовать переданный в функцию первый или единственный аргумент в десятичное число не удается,
		# 		то генерируется исключение `ValueError`, о котором мы говорили на строке 64.
		#
		#		Если вызвать функцию `int()` без аргументов, она вернет 0.
		#
		#		3.1 Что такое класс?
		#
		#			Классы и объекты в Python можно сравнить с описанием любимых питомцев.
		# 			Так, у каждого питомца есть имя, возраст, порода и другие характеристики.
		# 			Все эти атрибуты присущи классам в Python. То есть класс — это определенная сущность или набор атрибутов.
		# 			Например, если у животных набор атрибутов включает кличку, возраст и породу,
		# 			то у человека — имя, возраст, национальность, а у автомобиля — марку, модель, год производства.
		#
		#			```
		#			class Pet:
		#				def __init__(self, name, age, breed):
		#					self.name = name
		#					self.age = age
		#					self.breed = breed
		#			```
		#
		#			Объект — это воплощение класса.
		# 			Например, класс «домашние питомцы» включает в себя объект «котенок», который будет обладать точными атрибутами.
		#
		#			- Кличка: Мурка
		#			- Возраст: 2 месяца
		#			- Порода: британская длинношерстная
		#
		#			```
		#			kitten = Pet('Мурка', 0.2, 'british shorthair')
		#			```
		#
		#			*Заметка: в данных примерах используется синтаксис определения и вызова функций,
		#			о которых мы говорили на строке 85, секции 2.1, 2.2
		M = int(input('Введите массу в килограммах: '))

		# Те, кто знают английский, могут подумать, что слово "break" означает "ломать" или "перерыв",
		# но в контексте Python это не так.
		#
		# Вместо этого, `break` используются в случаях, когда нужно завершить цикл принудительно,
		# даже если его условие всё ещё выполняется, тем самым "сломать цикл" или дать ему "перерыв" - смотря какой Вы программист.
		#
		# Возьмём строку "Hi, loop!" и будем выводить каждый её символ. Если встретим запятую, досрочно завершим цикл.
		#
		# ```
		# string = 'Hi, loop!'
		# 
		# for i in string:
		#	if i == ',':
		#		break
		#	print(i)
		# ```
		#
		# Если же в строке запятой не будет, то цикл пройдёт по каждому её символу — и только потом завершится.
		break
	except ValueError:
		print('Введено некорректное число!\n')

print(f'Масса в полных тоннах: {M // 1000}')