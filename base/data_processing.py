#============= Обработка данных ===========
# Это работа с данными для получения полезной информации

grades = [4, 3, 5, 4, 3]
# Средний балл
# Минимальный балл
# Максимальный
# Посчитать колличество оценок

# =============== Фильтрация данных ===============
# Выбор по определенному условию

numbers = [1, 2, 3, 4, 5]
# Оставить только четные числа
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


# Дан список 
numbers = [23, 34, 56, 43, 12, 31]
# отфильтровать только те числа которые больше 20
result = []

for num in numbers:
    if num > 20:
        result.append(num)
print(result)

# Есть список слов
words = [
    "Кот", "программирование", 'дом', "компьютер", "наушники"
]
# отфильтровать только те слова у которых длина больше 5 символов

result = []
for word in words:
    if len(word) > 5:
        result.append(word)
print(result)


# ============= Агрегация функций =============
# Агрегация - получение итогового значение по набору данных
# (сумма, колличество элементов, среднее значение, масимум, минимум)

# Функция sum()
prices = [120, 290, 100, 50]
result_summ = sum(prices)
print(result_summ)

# Функция len()
length = len(prices)
print(length)

# Функция max
print(max(prices))

# Функция min
print(min(prices))

# Среднее значение
average = result_summ / length
print(average)

# дан список 
grades = [5, 4, 3, 2, 4, 5, 4, 3, 5]
# Найти сумму, максимум, минимум, срднее, колличество оценок, сколько 5
print(sum(grades))
print(max(grades))
print(min(grades))
print(sum(grades)/len(grades))
print(len(grades))
print(grades.count(5))

# ======== labmda ================
# это коротка анонимная(без имени) функция

def square(num):
    return num ** 2
print(square(5))

square_lambda = lambda num: num ** 2
print(square_lambda(6))

# Несколько параметров в lambda
add = lambda a, b: a + b
print(add(6, 3))

# Создать и запустить анонимную функцию для вычисления
# num * 5
multiply = lambda num: num * 5
print(multiply(4))

# =============== Функция map() =============
# Применяет функцию ко всем элементам списка
num_list = [1, 2, 3, 4]
result = map(
    lambda num: num ** 2, num_list
)
print(list(result))

# Увеличить все элементы на 10
num_list = [1, 2, 3, 4]
result = map(
    lambda num: num + 10,
    num_list
)
print(list(result))

# ============ Функция filter() ===========
nums = [1, 2, 3, 4, 5, 6]
result = filter(
    lambda num: num % 2 == 0,
    nums
)
print(list(result))

# офильтровать только те числа которые больше 3
nums = [1, 2, 3, 4, 5, 6]
result = filter(
    lambda num: num > 3,
    nums
)
print(list(result))


# ============== List comprehension ===========
# Это которткий способ создания списков

result = []
for i in range(1, 11):
    result.append(i)
print(result)

result_list = [i for i in range(1, 11)]
print(result_list)

square_list = [i**2 for i in range(1, 11)]
print(square_list)

# Создать лист компрехеншен от 1 до 100 и умножить каждый элемент на 2
double = [i*2 for i in range(1, 101)]
print(double)

# ===== Компрехеншены с условиями =========
a = True if 5 > 10 else False
print(a)
# Тернарный оператор это if/else в одну строчку
# но без elif
numbers = [1, 2, 3, 4, 5, 6]
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

multiply = [num ** 2 if num % 2 == 0 else num for num in numbers]
print(multiply)


numbers = [10, 15, 20, 25, 30]
# оставить только числа больше 20 используя List comprehension
result = [num for num in numbers if num > 20]
print(result)


result = [[[0 for i in range(3)] for i in range(3)] for i in range(3)]
print(result)