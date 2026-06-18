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