# ========= GROUP BY, HAVING, Агрегатные функции =========

# Основные агрегатные функции
1) AVG - среднее
2) COUNT - количество записей
3) SUM - вычисляет сумму
4) MIN/MAX - Минимум\Максимум

# COUNT
ПРИМЕР:
    SELECT COUNT(*) AS "Колличество курсов" FROM courses;

С условием:
    SELECT COUNT(*) AS "Колличество курсов" FROM courses WHERE price > 20000;


# Посчитать колличество курсов где ментора зовут Asan
SELECT COUNT(*) AS "Курсы ментора Асана" FROM courses WHERE teacher = 'Asan';

# SUM()
# Пример:
    SELECT SUM(duration) FROM courses;

# Посчитать сумму ценн всех курсов
SELECT SUM(price) FROM courses;


AVG - среднее
Пример:
    SELECT AVG(price) FROM courses;

# Посчитать среднюю продолжительность курсов
SELECT AVG(duration) FROM courses;

# Вытащить минимальную и максимальную цену
SELECT MIN(price) FROM courses;
SELECT MAX(price) FROM courses;
SELECT MIN(price), MAX(price), AVG(price) FROM courses;

# Вытащить количество студентов
# средний возраст
# вытащить колличество студентов которые старше 20
# вытащить мин\макс возраст

SELECT COUNT(*) FROM students;

SELECT AVG(age) FROM students;

SELECT COUNT(*) FROM students WHERE age > 20;

SELECT MIN(age), MAX(age) FROM students;


# ============= GROUP BY ================
# Синтаксис
    SELECT <столбец>, <агрегатная функция>
    FROM <table_name>
    GROUP BY <column_name>

# Пример: Количество курсов каждого препода
    SELECT teacher, COUNT(*)
    FROM courses
    GROUP BY teacher;

# Вытащить среднюю стоимость курсов по преподам
SELECT teacher, AVG(price)
FROM courses
GROUP BY teacher;

# Общаю продолжительность кусов у каждого ментора
SELECT teacher, SUM(duration) FROM courses
GROUP BY teacher;

# вычислить максимальную стоимость по каждому ментору
SELECT teacher, MAX(price) FROM courses
GROUP BY teacher;

# Количество студентов в группах
SELECT group_name, COUNT(*)
FROM students
GROUP BY group_name;

# ВАЖНОЕ ПРАВИЛО!!!!!
Если столбец передается(указан) в SELECT и оно не является агрегатной функцией,
то он у нас обьязательно должен присуствовать в GROUP BY


# ------- HAVING ------
WHERE                       VS              HAVING
работает до группировки                     работает после группировки

# Пример
вытащить преподов у которых больше 2 курсов
SELECT teacher, COUNT(*)
FROM courses
GROUP BY teacher
HAVING COUNT(*) > 1;

# Вытащить менторов у которых срредняя цена выше 20000
SELECT teacher, AVG(price)
FROM courses
GROUP BY teacher
HAVING AVG(price) > 20000;

# Вытащить менторов у которых общая продолжительность курсов больше 8
SELECT teacher, SUM(duration)
FROM courses
GROUP BY teacher
HAVING SUM(duration) > 8;


# ----- WHERE + HAVING ------
1) вытащить курсы у которых стоимость больше 15000
2) показать менторов у которых средняя цена больше 22000

    SELECT teacher, AVG(price)
    FROM courses
    WHERE price > 15000
    GROUP BY teacher
    HAVING AVG(price) > 22000;

# Вытащить всех менторов кроме ментора Asan и также у кого максимальная стоимость кусов выше 18000
SELECT teacher, MAX(price)
FROM courses
WHERE teacher != 'Asan'
GROUP BY teacher
HAVING MAX(price) > 18000;