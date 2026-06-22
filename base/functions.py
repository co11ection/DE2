# ========== Функции ==============
# Фуункция - именованный блок кода, который принимает аргументы 
# и возвращает результат
# def - инициализация\создание функции

# Функция соблюдает принцип DRY (don't repeat yourself)

a = 5
b = 6
print(a + b)

def my_sum(a, b):
    result = a + b
    return result
    
result_function = my_sum(a=5, b=6)

print(result_function)

""" 
def <название функции>(<параметры>)
    <логика\ тело функции>
    return <результат> 'если не прописать вернет None'

<название функции>(<аргументы>)
"""
# ========== Аргументы и параметры ============
"""
Параметры - переменные внутри функции, значение которым задаем при вызове функции
def name_function(параметры)


Аргументы - значения которые мы передем при вызове функции
my_sum(аргументы)
"""

# ============= Виды параметров =============
"""
1 - обьязательные
2 - необязательные
    2.1 - дефолтные
    2.2 - args - все позиционные аргументы которые не попали в обьязательные
    или дефолтные параметры попадают в args, принимает в виде tuple
    2.3 - kwargs - все именованные аргументы которые не попали в обьязательные
    или дефолтные параметры попадают в kwargs, принимает в виде dict
"""
# ============ Виды аргументов ==============
"""
1 - Позиционные (по пазициям)
2 - именованные (по названию параметра)
"""

def my_sum(a, b): # Обьязательные параметры
    result = a + b
    return result
    
print(my_sum(a=5, b=6)) # Именованные
print(my_sum(5, 6)) # Позиционные

# Дефолтные
def func(a, b, c=7):
    return a + b + c

print(func(a=2, b=3))
print(func(a=2, b=3, c=3))

def func(a, b, *args):
    print("a ->" , a)
    print("b ->", b)
    print("args ->", args)
    
func(1, 2, 4, 5, 5, 6, 7, 2, 8)
# a -> 1
# b -> 2
# args -> (4, 5, 5, 6, 7, 2, 8)


def func(a, b, **kwargs):
    print("a ->" , a)
    print("b ->", b)
    print("kargs ->", kwargs)
    
func(a=3, b=4, c=4, d=7, g=9)


def multiply(num1, num2):
    return num1 * num2

print(multiply(2, 3))


# Написать функцию is_even(num)
# возвращать True если четное и False если не четное
def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(4))
print(is_even(5))

# =============== Практика ===========
# создать функцию factorial(num), вернуть факториал числа
# 5! -> 1 * 2 * 3 * 4 * 5
def factorial(num):
    result = 1
    for n in range(1, num+1):
        result *= n
    return result

print(factorial(5)) # 120
print(factorial(6)) # 720

# Напишите функцию sum_list(num_list)
# которая возвращает сумму всех чисел списка 
def sum_list(num_list):
    result = 0
    for num in num_list:
        result += num
    return result
    
num_list = [1, 2, 3, 4]
print(sum_list(num_list))

# Написать функцию is_palindrome(word),
# проверять является ли слово полиндромом
# если да то вернуть True если нет то False

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

print(is_palindrome('Level'))
print(is_palindrome('taxi'))

