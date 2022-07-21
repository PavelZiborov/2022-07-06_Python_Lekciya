# Работа с Файлами

# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a - открытие для добавления данных (добавляет все новые и новые данные в существующий файл)
# r - открытие для чтения данных
# w - открытие для записи данных (перезаписывает все данне в файле на нужные)
# w+, r+ 


from itertools import count


colors = ['red', 'green', 'blue3123']

# Первый способ добавления данных в файл:
# data = open('file.txt', 'a') # открывает файл для добавления данных
# data.writelines(colors) # дописывает в него переменную colors. Разделителей не будет
# data.write('LINE 121\n') # \n добавляет перенос на новую строку
# data.write('LINE 131\n')
# data.close

# Второй способ добавления данных в файл:
with open('file.txt', 'w') as data:
    data.write('line 1111\n')
    data.write('line 2222\n')

# exit() # выход из программы. Дальше код не будет выполняться


# Чтение данных из файла
path = 'file.txt' # создаем путь к файлу
data = open(path, 'r') # открываем в режиме чтения
for line in data: # пробегаем циклом по всем строчкам и печатаем их (читает строчку)
    print(line)
data.close()



# Использование функционала из другого файла
import lec01 # импортируем в этот код, код из соседнего файла
print(lec01.f(1)) # вызываем печать функции, которая находится в другом файле

import lec01 as L1 # можно файлу дать краткое или более удобное название через 'as'
print(L1.f(2)) # и тогда вызов этого файла уже будет проще

# Функция
def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12
print()

def concatenatio(*params): # * звездочка перед параметрами - любое количество параметров
    res: str = ""          # явное задание типа данных через двоеточие
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))   # asdw
print(concatenatio('a', '1'))             # a1
# print(concatenatio(1, 2, 3, 4))         # TypeError
print()

# Кортеж (tuple) - неизменяемый "список"

a = (3, 1, 41, 4) # Объявление кортежа через скобки ()
print(a)          # (3, 1, 41, 4)
print(a[-2])      # 41
# a[0] = 12       # TypeError. Кортеж нельзя изменять

t = ()
print(type(t))                      # tuple
t = (1,)
print(type(t))                      # tuple
t = (1)
print(type(t))                      # int
t = (28,9,1990)
print(type(t))                      # tuple
colors = ['red', 'green', 'blue']   # ['red', 'green', 'blue']
t = tuple(colors)
print(t)                            # ('red', 'green', 'blue')

for item in a:
    print(item)

# Словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {} # объявление словаря через фигурные скобки {}
dictionary = \
    {
        'up': '^',
        'left': '<',
        'down': 'v',
        'right': '>'
    }
print(dictionary)             # {'up': '^', 'left': '<', 'down': 'v', 'right': '>'}
print(dictionary['left'])     # <

for v in dictionary:       # dictionary.keys() - ключи, dictionary.values() - значения
    print(dictionary[v])   # dictionary[v] - значения, v - ключи

print(dictionary['up'])    # печатает значение по ключу up
dictionary['up'] = '123'   # можно заменить значение по конкретному ключу
print(dictionary['up'])

# dictionary.keys() - ключи
# dictionary.values() - значения
# dictionary.items() - все значения словаря (и ключи и значения)



# Множества - содержит уникальные элементы <class 'set'>

colors = {'red', 'green', 'blue'}
print(colors)                           # {'red', 'green', 'blue'}
colors.add('red')                       # # пытаемся добавить в множество 'red', но т.к. он уже есть, он его не продублирует
print(colors)                           # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)                           # {'green', 'gray', 'red', 'blue'}
colors.remove('red')
print(colors)                           # {'green', 'gray', 'blue'}
# colors.remove('red')
# print(colors)                         # KeyError: 'red' (ошибка т.к. такого элемента нет в множестве)
# ok .discard удаляет элемент, но если если такого элемента нет, но метод не вызовет ошибку
colors.discard('red')
print(colors)                           # {'green', 'gray', 'blue'}
colors.clear()                          # {} удаляет все элементы множества
print(colors)                           # set()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                  # a.copy() - копирует множество a
print(c)                      # c = {1, 2, 3, 5, 8}
u = a.union(b)                # a.union(b) - объединяет множество a с множеством b
print(u)                      # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)         # a.intersection(b) - пересечение множеств a и b
print(i)                      # i = {8, 2, 5}
dl = a.difference(b)          # разность (объекты, принадлежащие А, а не B)
print(dl)                     # dl = {1, 3}
dr = b.difference(a)          # разность (объекты, принадлежащие B, а не A)
print(dr)                     # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)                      # q = {1, 21, 3, 13}