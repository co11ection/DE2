# ================ CASE =============
# Условная логика работает так же как if/else

# Синтаксис
SELECT .....
    CASE
        WHEN <Условие> THEN <результат>
        ......
        ELSE <результат по умолчанию>
    END
FROM <tablename>

# Пример
# Категория курсов
    SELECT course_name, price,
        CASE 
            WHEN price < 15000 THEN 'Бюджетный' 
            WHEN price BETWEEN 15000 AND 20000 THEN 'Средний'
            ELSE  'Дорогой'
        END as price_category
    FROM courses

# Надо разделить по категориям студентов в зависимоти возраста
# до 21 - молодеж
# 21 до 23 - типо взрослые
# 23 выше - взрослые

    SELECT first_name, age,
        CASE 
            WHEN age < 21 THEN 'молодеж' 
            WHEN age BETWEEN 21 AND 23 THEN 'типо взрослые' 
            ELSE  'взрослые'
        END AS age_group
    FROM students


# =============== Строковые функции ================
UPPER()/LOWER() - В ВЕРХНИЙ РЕГИСТР\ НИЖНИЙ
LENGTH() - длина строки
CONCAT() или `\|\|`  - Склеивание строк
SUBSTRING(str FROM start FOR len) Вырезать строку
TRIM() - убитрает пробелы по краям
REPLACE(str, from, to) - замена подстроки
LIKE - поиск по шаблону (чуствителен к регистру)
ILIKE -  поиск по шаблону (не чуствителен к регистру)

# Обьединение
SELECT first_name || ' ' || last_name AS full_name FROM students
# Поиск с LIKE
SELECT * FROM students WHERE first_name LIKE 'A%'
# Поиск с ILIKE
SELECT * FROM students WHERE first_name ILIKE 'a%'
# REPLACE
SELECT REPLACE(course_name, 'DE', 'DS') FROM courses
