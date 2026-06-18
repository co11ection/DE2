#=================== Dict ================
# Словари - ключ: значение
# Литералы(Обозначение) {key: value, ...}

# !!!!!!!!! ОЧЕНЬ ВАЖНО !!!!!!!!!!!!!
# Клячами могут выступать только не изменяемые типы данных

# dict1 = {
#     ['hello', 'hi'] : "привет"
# }

# print(dict1)

# a = 5
# b = 5
# print(id(a))
# print(id(b))

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))

student_info = {
    'name': 'Asan',
    "age": 20,
    "city": "Bishkek"
}
# name --- ключ
# Asan --- значение

print(type(student_info))
print(student_info)

# Получение значения по ключу
print(student_info['name'])
print(student_info['age'])
print(student_info['city'])
# print(student_info['hi']) KeyERROR ключа нету
print(student_info.get('name'))
print(student_info.get('hi')) # None
print(student_info.get('hi', "Ключа такого нету")) # Ключа такого нету

# Изменение словаря
student_info['age'] = 21
print(student_info)

# Добавление нового ключа и значение
student_info['course'] = 2
print(student_info)

# Удаление
del student_info['age']
print(student_info)

# вытащить все значения(value)
print(student_info.values()) #dict_values(['Asan', 'Bishkek', 2]) 

# Вытащить все ключи(key)
print(student_info.keys()) #dict_keys(['name', 'city', 'course'])

# Все ключи и значение парами
print(student_info.items()) #dict_items([('name', 'Asan'), ('city', 'Bishkek'), ('course', 2)])

book = {
    "title": 'Убийство в поезде',
    "author": "Агата кристи",
    "year": 1995
}
# 1 вывести название книги
# 2 изменить год
# 3 добавить жанр
# 4 вывести словарь полностью, и все ключи и значения

print(book['title'])
print(book.get('title'))
book['year'] = 1980
print(book)
book["genre"] = "detective"
print(book)
print(book.items())

# ================ SET ===========================
# Множества - коллекция(список) с уникальными элементами(данными)
# уникальные, изменяемый, не упорядочный, не индексируемый
set1 = {"hello", 'яблоко', 'банан'}
print(type(set1)) #<class 'set'>

set2 = {1, 1, 2, 2, 3, 4, 4}
print(set2) #{1, 2, 3, 4}

# Добавление
fruits = {"яблоко", 'банан'}
fruits.add("груша")
print(fruits)

# удаление
fruits.remove("банан")
print(fruits)


# Обьединение двух set
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Пересечение
print(a & b) # {3}


# ================== TUPLE ================
# Кортежи - не изменяемый тип данных, тот же самый list
# Литералы(обозначение) - (,)
# индексируемый, упорядочный
nums = (1, 2, 3, 4)
print(type(nums)) # <class 'tuple'> 

print(nums[0])
print(len(nums))

# nums[0] = 10
# print(nums) ERROR

# Отличие tuple от list

# tuple           list
# неизменяемый    изменяемый
# быстрее         медленне

countries = (
    "Кыргызстан",
    "Казахстан",
    "Узбекистан",
    "Россия",
    "Америка"
)
# 1 Вывести первый элемент
# 2 вывести колличество
# 3 сделать срез вывести страны средней азии

print(countries[0])
print(len(countries))
print(countries[0: 3])


car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022
}

# вывести модель
# изменить гол
# добавить цвет

print(car['model'])
print(car.get('model'))
car['year'] = 2024
print(car)
car['color'] = 'white'
print(car)