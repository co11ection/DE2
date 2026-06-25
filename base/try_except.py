# ========= Ошибки и Исключения и обработка их ============
# Ошибка - когда программа не может продолжить работу

# ========= Виды ошибок ==========
# 1) Синтаксическая ошибка - возникает когда не правильно написан код
# if 5 > 3  #- нету :
#     print("hello")
#     SyntaxError: expected ':'

# 2 Ошибка выаолнения(Runtime Eror)
# Код прописан правильно но возникает проблема самого выполнения
# print(10/0) # ZeroDivisionError

# 3 Логические ошибки
# Программа работает но выдает неверный результат
# проверить num меньше 20
num = 20
if num <= 20:
    print("привет")
# Ожидалось проверка просто меньше, но выдалось проверка на меньше или равно

# ====== Исключения ===========
# Все ошиьбки которые можно обработать считается исключением
# ValueError - Несоответсвие типов данных
# age = int("hello")

# ZeroDivisionError - При делении на ноль
# print(10/0)

# NameError - Когда такого названия (переменной) в файле не существует
# print(name)

# IndexError - Индекса такого не существует
# numbers = [1, 2, 3]
# print(numbers[10])

# KeyError - когда ключа такого нету в словаре
# student = {
#     "name": "Asan",
#     "age": 20
# }

# print(student['email'])


# ======== Практика ============ 
# print(age) - NameError
# print(23/0) - ZeroDivisionError
# print(int('hhho')) - ValueError

# ========== Обработка Исключений======
# Конструкция try/except
# Обработка ошибок(исключений)
# user_number = int(input("Введите число: "))
# print(user_number)

# try:
#   выполняемая программа
# except <какое исключение>:
#   что вернуть при выбросе исключения

# Если ошибки нету - выполнится то что внутри try
# Если возникает ошибка - то выполнится то что внутри except
# try:
#     user_number = int(input("Введите число: "))
#     print(user_number)
# except ValueError:
#     print("ValueError: Ошибка обработки типа данных")
    
# print("hello")

# Несколько исключений и вывод разных ошибок
numbers = [1, 2, 3, 4, 5]
# try:
#     user_number = int(input("Введите число: "))
#     print(numbers[user_number])
# except ValueError:
#     print("ValueError: Ошибка обработки типа данных")
# except IndexError:
#     print("IndexEror: такого индекса не существует")


# Получение текста ошибки
# try:
#     user_number = int(input("Введите число: "))
#     print(numbers[user_number])
# except ValueError as error:
#     print(error)
# except IndexError:
#     print("IndexEror: такого индекса не существует")
    

# Написать программу деления двух чисел
# обработать ошибку ZeroDevisionError

try:
    num1 = 0
    num2 = 10
    print(num2/num1)
except ZeroDivisionError:
    print("ZeroDivisionError: На 0 делить нельзя!!!!!!")

# запросить у пользователя возраст
# обработать ошибку не правильного ввода
# try:
#     age = int(input("Введите возраст: "))
#     print(f"Возраст: {age}")
# except ValueError:
#     print("ValueError: Не верный ввод")
    
# Блокие else и finally
# блок else: - выполняется только тогда когда ошибки нету

# try:
#     age = int(input("Введите возраст: "))
#     print(f"Возраст: {age}")
# except ValueError:
#     print("ValueError: Не верный ввод")
# else:
#     print("Успешно отработало")
    
# Finally - он работает в любом случае
# try:
#     age = int(input("Введите возраст: "))
#     print(f"Возраст: {age}")
# except Exception as e:
#     print(e)
# else:
#     print("Успешно отработало")

# finally:
#     print('Программа завершилась')
    
    
# ===== Генерация исключений raise ======
# age = int(input("Введите возраст: "))
# if age < 0:
#     raise ValueError("Возраст не может быть меньше 0")


# Получить от пользователя пароль и проверить длину пароля, 
# должно быть не меньше 6 символов
# password = input("Введите пароль: ")
# if len(password) < 6:
#     raise ValueError("Пароль не может быть меньше 6 символов")

# =========== Логирование =================
# логирование - запись событий
# INFO, WARNING, ERROR

import logging
logging.basicConfig(
    level=logging.INFO,
    filename='app.log'
)

logging.info(
    "Программа запущена"
)

logging.warning(
    "Памяти мало"
)

logging.error(
    "Ошибка программы"
)


try: 
    result = 10/0
except ZeroDivisionError:
    logging.error("Деление на ноль")