# Типы данных и переменная
# int, float, booleat, str, list, None
'''
value = None
print(type(value))
# print(type(a))
# print(type(b))
value = 1234
# print(type(value))
a = 123
b = 1.23
s = 'hellow world'
print(s)  # вывод строки
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))  # вывод интерполяцией
print(f'{a} - {b} - {s}')  # вывод интерполяцией (перед кавычками поставить f)
print('{1} - {2} - {0}'.format(a, b, s))  # вывод интерполяцией

f = False
print(f)

list = ['1', '2', '3']  # объявление листов (массивов)
col = ['hellow', 1, 2, 3, False]

print(list)
print(col)

# print('Введите А')
# a = float(input())  # перед input ставим тип для явного указания типа
# print('Введите B')
# b = float(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# орифметические операции
# +, -, *, (стандартные сложение, вычитание, умножение)
# / (деление для вещественных чисел),
# // (деление в целых числах),
# % (остаток от деления),
# ** (возведение в степень)
# Сокращение операции a = a + 5 это тоже самое что и a += 5

a = 1.3123
b = 3
# функция round округляет по математическим правилам (через запяную указать количество цифр после запятой)
c = round(a * b, 5)
print(c)

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
#

a = 1 < 4 and 1 > 19
print(a)
a = 1 != 1
print(a)
a = [1, 2]
b = [1, 2]
print(a == b)

a = 1 < 3 < 5  # тройные сравнения
print(a)

func = 1
T = 4
x = 2
print(func < T > x)

f = 1 > 2 or 4 < 6
print(f)

f = [1, 2, 3, 4]
print(f'2 in f = {2 in f}')
print(f'not 2 in f = {not 2 in f}')

# (f[0] % 2 == 0) - проверяем остаток от деления на 2 (истина или ложь)
is_odd = not f[0] % 2
print('is_odd =', is_odd)

# логические ветвления if esle
# if condition:
# operator 1
# operator 2
# else:
# operator n + 1
# operator n + 2
# ОТСТУПЫ ВАЖНЫ

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# блок использования if elif else
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)

# управляющая конструкция while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original = original // 10  # можно записать как: original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

# Управляющая конструкция for
# for i in enumeration: (итерируемый объект (список))
    # operator 1
    # operator 2

for i in 1, 2, 3, 4, 5:
    print(i**2)

list = [1, 2, 3, 10, 5]
for i in list:
    print(i**2)

r = range(10) # выдает итератор от 0 до 9 если просто указать 10.
r = range(10, 20) # если перечислить через запятую - выдет перечисление от первого числа до второго
r = range(10, 20, 2) # если добавить третий аргумент, то он показывает приращение (т.е. +2)
for i in r: # или for i in range(10):
    print(i)
for i in 'qwerty': 
    print(i)

# немного о строках
text = 'съешт еще этих магких французских булок'
print(len(text))                  # 39
print('еще' in text)              # True
print(text.isdigit())             # False (проверяет все ли элементы являются числами)
print(text.islower())             # True (проверяет все ли элементы написаны на нижнем регистре)
print(text.replace('еще', 'ЕЩЕ')) # заменяет одну строку на другую

# help(str) - справка

print(text[0])                    # с
print(text[1])                    # ъ
# print(text[len(text)])          # IndexError
print(text[len(text) - 1])        # к
print(text[-5])                   # б (последний символ имеет индекс -1)
print(text[:])                    # напечатает все элементы с 0 до последнего
print(text[0:2])                  # съе
print(text[2:9])                  # ешь еще
print(text[6:-18])                # еще этих мягких
print(text[0:len(text):6])        # сеикакл
print(text[::6])                  # сеикакл
text = text[2:9] + text [-5] + text[:2] # ...
'''

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return