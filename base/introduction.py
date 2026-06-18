# =================== Переменная =============
# Переменная - сундук с вещами внутри

name = "Nurbek"
# 2name - нельзя
# name2  - можно
age = 23
print(name, age)

# Практика
# name
# surname
# age
# city


# ================== Типы данных =============
# 1) Изменяемые                 2 Неизменяемые
    #list - список             int -  целое число
    #dict - словарь            float - число с плавающей точкой(10.5)
    #set - множества           tuple - кортежи 
                                # str - строка
                                # bool - True/False
                                
# ================== INT ====================
num = 20
num2 = 30
# Операторы
# +           сложение
# -           вычитание
# *           умножение
# /           деление с остатком
# //          деление без остатка
# %           остаток
# **          возведение в степень

num = 10
num2 = 3

print(num+num2)

result = num + num2
print(result)

# =============== Строки ==============
# Создание строки
# '', "" - обозначение строки

text = "Hello world"
print(type(text)) # вывод типа данных
print(type(num))
print(type(10.5))

print(len(text)) # длина строки - 11

# Индексы
" H e l l o"
# 0 1 2 3 4
text = "Python"
"nohtyP"
print(text[0])
print(text[2])
print(text[5])
print(text[-1])
#  Срезы
print(text[0:2]) # Py
print(text[2:]) # thon
print(text[::-1]) #"nohtyP"

print(text[::2]) #Pto

# Конкатенация (сложение строк)
text1 = "Hello"
text2 = "world"

print(text1 + text2) #Helloworld

name = 'Nikita'
print('Имя ' + name) #Имя Nikita

a = '5'
b = '6'
print(a+b)

# Повторение строк
a = 'hi'

print(a * 3) #hihihi

text = "python"
print(text.upper()) #PYTHON
text2 = "PYTHON"
print(text2.lower()) #python

print(text.replace("o", '0')) # pyth0n

text = 'ololololo'
print(text.replace("o", "u", 3)) #ulululolo

word = 'Programming'
#1 вывести длину строки
#2 вывести первый символ
#3 вывести последние 3 символа
#4 перевести все на верхний регистр

print(len(word))
print(word[0])
print(word[-3:])
print(word.upper())


# ============== Списки ===============
# [] - литералы(обозначение) списков(list)
list_elements = [1, 2, 15.6, 'hello', True]
print(list_elements[0]) # 1

# Изменение
list_elements[1] = 3
print(list_elements)

# Добавление
list_elements.append('world')
# Добавление
print(list_elements) #[1, 3, 15.6, 'hello', True, 'world']

# удалить последний элемент
removed = list_elements.pop()
print("удаленный элемент", removed)
print(list_elements)

# Удалить по элементу
list_elements.remove(15.6)
print(list_elements)


print(3 in list_elements)
print(10 in list_elements)


fruits = ['яблоко', 'банан', 'апельсин']
# 1) вывести первый элемент
# 2) добавить груша
# 3) удалить банан
# 4) вывести длину списка

print(fruits[0])
fruits.append("груша")
fruits.remove('банан')
print(fruits)
print(len(fruits))