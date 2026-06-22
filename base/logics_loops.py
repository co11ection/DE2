# ===============  Условные операторы =============
# оператор if
# Синтаксис
#   if <условие>:
#       действие

age = 20

if age >= 18:
    print("Совершеннолетний")
    
# Операторы if - else
# "18" - строка
# 18 - число

# age = int(input("Введите возраст: ")) # 18 -> "18"
# if age >= 18:
#     print("совершеннолетний")
# else:
#     print("не совершеннолетний")
    

# # Операторы if - elif - else
# if age >= 70:
#     print('pensioner')

# elif age < 18:
#     print("child")

# elif age >= 18:
#     print("adult")
    

# Построить условия 
# score = 
# если балл выше 90 то Отлично
# выше 70 хорошо
# выше 50 удовлетворительно
# в ином случае Неудовлетворительно

score = 56

if score > 90:
    print("Отлично")
elif score > 70:
    print("хорошо")
elif score > 50:
    print("удовлетворительно")
else:
    print("Неудовлетворительно")
    

# Вложенные условия
student_info = {
    "name": "Asan",
    "age": 20,
    "is_student": False
}

if student_info.get("age", 0) > 18:
    if student_info.get("is_student", False) == True:
        print(f"Студент {student_info.get("name")} старше 18 лет")
    else:
        print(f"{student_info.get("name")} не является студентом")


# Логические операторы
# and - и 
# оба условия должны возвращать True
# True and False = False
# True and True = True

student_info = {
    "name": "Asan",
    "age": 20,
    "is_student": True
}

if student_info.get("age", 0) > 18 and student_info.get("is_student") == True:
    print(f"Студент {student_info.get("name")} старше 18 лет")
else:
    print(f"{student_info.get("name")} не является студентом")

# or - или
# Хотябы одно условие True
# True or False = True
# True or True = True
# False or False = False

student_info = {
    "name": "Asan",
    "age": 16,
    "is_student": False
}

if student_info.get("age", 0) > 18 or student_info.get("is_student") == True:
    print(f"Студент {student_info.get("name")} старше 18 лет")
else:
    print(f"{student_info.get("name")} не является студентом")
    
    
# not - Изменяет значение на противоположное
# True ---> False
# False ---> True

is_student = False
if not is_student == True:
    print("Не стуудент")
else:
    print("студент")
    

# ============== Практика ============
# Пользователь вводит число
# Определить: Полождительным или отрицательным или же равно нулю

user_number = int(input("Введите число: "))

if user_number > 0:
    print("Число положительное")
elif user_number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
    
# Д/З
# написать калькулятор



# ================== Циклы =====================
print("Привет")
print("Привет")
print("Привет")
print("Привет")
print("Привет")
print("Привет")
print("Привет")
print("Привет")
# более 200
# Цикл - Повторение одного и того же кода многократно
# Цикл делится на 2 вида: for, while


# ============= for ==============
# Цикл for проходит по итерирууемым обьектам или типам данных(
# list, dict, set, str, tuple   
#)
# Итерация - повторение

for i in range(1, 201):
    print(f"{i} Привет!")
    
    
# Вывести числа от 1 до 10

for i in range(1, 11):
    print(i)
    

# вывести числа от 10 до 1

for i in range(10, 0, -1):
    print(i)
    
# Вывести только четные числа от 1 до 20 включительно
print("!!!!!!!!!!!")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        
# Перебор строки
word = "Python"
for letter in word:
    print(letter)
    
# вывести по буквам слово "Программирование"
word = "Программирование"
for letter in word:
    print(letter)

# Перебор списка
fruits = ['apple', 'banan', 'grape', 'pear']
for fruit in fruits:
    print(fruit)
    

animals = [
    'кот',
    'собака',
    'хомяк',
    'лев'
]

for animal in animals:
    print(animal)
    

# Сумма чисел от 1 до 5
total = 0
# total = total + num
# total += num
for num in range(1, 6):
    total += num
    print(total)
    
# найти сумму всех четных чисел от 1 до 50
total = 0
for num in range(1, 51):
    if num % 2 == 0:
        total += num
        
print(total)

# ================ While =============
# бесконечный цикл
# Синтаксис
# while <условие>:
#     действие

num = 1

while num <= 10:
    print(num)
    num += 1
    

# вывести числа от 1 до 20

num = 1

while num <= 20:
    print(num)
    num += 1



# выести числа от 20 до 1

num = 20

while num != 0:
    print(num)
    num -= 1
    
password = ''

# while password != 'python':
#     password = input("Введите пароль: ")
    
# print("Вы вошли в систему")


# Пользователь вводит число пока не введет 0

user_number = None

while user_number != 0:
    user_number = int(input("Введите число: "))
    

# Оператор break
# оставливает цикл

for i in range(10):
    if i == 5:
        break
    else:
        print(i) 
        

# Оператор contiune
# Пропускает одну итерацию

for i in range(1, 10):
    if i == 3:
        continue
    else:
        print(i)


# вывести число 1 до 20 кроме 5, 10, 15
for i in range(1,21):
    if i == 5 or i == 10 or i == 15:
        continue
    else:
        print(i)

print('!!!!!!!!!!')

for i in range(1, 21):
    if i in [5, 10, 15]:
        continue
    else:
        print(i)
        
        
#НЕ ДЕЛАЙ ТАК
# while True:
#     print(1)


# list1 = [1, 2, 3, 4]
# for i in list1:
#     list1.append(i)
#     print(list1)