# Упражнение 1
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

# name = input('Введите ваше имя')
# age = int(input('Введите свой возраст'))
# sex = input('Введите Ваш пол ')
# city = input('Введите название города где Вы проживаете')
# print('Вас зовут', name, '.', 'Вам', age, 'лет.', 'Вы', sex, '.','ВЫ проживаете в городе', city, '.')
# ----------------------------------------------------------------------------------------------------------------
# Упражнение 2
# Пользователь вводит время в секундах. Время в часах, минутах, секундах
# выведите в формате чч:мм:сс. использовать форматирование строк.

# time = int(input('Введите количество секунд: '))
# hour = time//3600
# minutes = (time - hour*3600)//60
# second = time - ((minutes*60)+(hour*3600))
# print(f'Преобразование секунд в часах,минутах,секундах выражено: {hour:02}:{minutes:02}:{second:02}')
# ---------------------------------------------------------------------------------------------------------------
# Упражнение 3
# встречается у пользователя число n. Появляются суммы чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

# n = int(input('Введите число: '))
# number = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# print('Сумма n+nn+nnn равна ', number)
# -----------------------------------------------------------------------------------------------------------------
# Упражнение 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

# money = int(input('Включить значение прибыли компании в $: '))
# expenses = int(input('Ввести значение издержек компании в $: '))
# profit = money - expenses
# if money >= expenses:
#     print(f'Компания работает в прибыль. Чистая прибыль составляет: {profit}$')
#     rent = money / profit
#     print(f'Рентабельность компании состоит: {rent:.2f}')
# else:
#     print(f'Компания работает в убыток. Убыток составляет: {profit}$')
#     if money >= expenses:
#         people = int(input('Введите количество сотрудников фирмы: '))
#         profit2 = profit / people
#         print(f'Прибыль фирмы в расчете на одного сотрудника: {profit2:.2f}$')
# -----------------------------------------------------------------------------------------------------------------
# Упражнение 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

# a = int(input('Введите расстояние в километрах за первый день пробежки: '))
# b = int(input('Введите результат, которые пробежит спортсмен: '))
# i = 1
# print(f'{i}: {a}')
# while a <= b:
#     a = a + (a * 0.1)
#     i = i + 1
# print(f'{i}: {a:.02f}')
# print(f'На {i}-й день спортсмен достиг результата - не менее {b} км. ')
