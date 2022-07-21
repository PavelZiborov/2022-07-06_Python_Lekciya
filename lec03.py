# lambda функции


def f(x):
    return x**2

g = f  # переменная которая хранит ссылку на функцию
print(type(f))
print(type(g))
print(f(1))
print(g(2))

def calc1(x):
    return x+10
print(calc1(10))

def calc2(x):
    return x*10
print(calc2(10))

def math(op, x):
    print(op(x))
math(calc2, 5)

# Эту запись функции можно записать так:
# def sum(x, y): 
#     return x+y

# А можно так:
# sum = lambda x, y: x+y # вот так

def mylt(x, y):
    return x*y

def calc(op, a, b):  # в качестве аргумента может быть целая функция
    print(op(a, b))
    return op(a, b)

calc(lambda x, y: x+y, 4, 3)  # в качестве аргумента передаем функцию mylt


# Простое создание списков
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item int iterable (if conditional)]

# Обычное создание списка из четных чисел от 1 до 100
list1 = []
for i in range(1,11):
    # if (i%2 == 0):
    list1.append(i)
print(list1)

# Другая запись:
list2 = [i for i in range(1,11)]
print(list2)

# Другая запись (добавляем условие добавления в список):
list3 = [i for i in range(1,11) if i%2 == 0]
print(list3)

# Другая запись (добавляем в список кортежи):
list4 = [(i,i) for i in range(1,11) if i%2 == 0]
print(list4)

def f(x):
    return x**3

# Другая запись (записываем в список результат вычисления функции):
list4 = [(i,f(i)) for i in range(1,11) if i%2 == 0]
print(list4)

# Задача (как решил ее я)
list4 = [1,2,3,5,8,15,23,38]
list5 = [(i,i**2) for i in list4 if i%2 == 0]
print(list5)

# Как решил ее Сергей
def select(f,col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data) # это (уже не нужно описание функции select)
res = list(map(int, data)) # и это одно и тоже 

res = where(lambda x: not x%2, res)
# res = list(filter(map(lambda x: not x%2, res))) # функция filter() заменяет функцию where 

res = select(lambda x: (x, x**2),res)
# res = list(map((lambda x: (x, x**2),res)))

print(res)

# функция map
li = [x for x in range(1,11)]
li = list(map(lambda x: x+10, li))
print(li)

data = list(map(int, '1 2 5 111'.split())) # list() приводит объект map к листу (сохраняет принудительно в список)
print(data)

# функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с тему объектами, для
# которых функция вернула True.

data2 = [x for x in range(10)]

res2 = list(filter(lambda x: not x % 2, data2))
print(res2)

# Функция zip() применяется к набору итерируемых объектов и 
# возвращает итератор с кортежами из элементов входных данных.