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
# import lec01 # импортируем в этот код, код из соседнего файла
# print(lec01.f(1)) # вызываем печать функции, которая находится в другом файле

# import lec01 as L1 # можно файлу дать краткое или более удобное название через 'as'
# print(L1.f(2)) # и тогда вызов этого файла уже будет проще

# Функция
def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12
print()

def concatenatio(*params):
    res: str = ""          # явное задание типа данных через двоеточние
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))   # asdw
print(concatenatio('a', '1'))             # a1
# print(concatenatio(1, 2, 3, 4))         # TypeError
print()

# Кортеж (tuple - неизменяемый "список"
a = (3, 1, 41, 4) # Объявление кортежа
print(a)          # (3, 1, 41, 4)
print(a[-2])      # 41
# a[0] = 12       # TypeError. Кортеж нельзя изменять

for item in a:
    print(item)