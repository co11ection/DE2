# =========== Подзапросы ===============
# SQL запрос внутри другого SQL запроса
SELECT column_name FROM(
    SELECT ....
)

или

SELECT * FROM table_name WHERE (
    SELECT .....
)
# Подзапрос - можно представить как временный результат, который использует основной запрос

# Найти курс с максимальной ценой
SELECT * FROM courses
WHERE price = (
    SELECT MAX(price)
    FROM courses
)

# Найти преподавателя с самой большой зарплатой
SELECT * FROM teachers
WHERE salary = (
    SELECT MAX(salary)
    FROM teachers
)


# Найти студентов курса "DE"
SELECT * FROM students
WHERE course_id = (
    SELECT id FROM courses
    WHERE course_name = 'DE'
)


# Подзапрос с IN
# Найти студентов которые учатся на курсах дороже 15000

SELECT * FROM students
WHERE course_id IN (
    SELECT id FROM courses
    WHERE price > 15000
)


# ------- Подзапрос в FROM -------
Подзапрос будет рассматриваться как временная таблица

# Найти курсы дороже 15000
SELECT * FROM (
    SELECT course_name, price
    FROM courses
    WHERE price > 15000
) expensive_course;

# --------- Подзапросы с SELECT -------
SELECT course_name, price, (
    SELECT AVG(price) FROM courses
) AS average_price
FROM courses


# -------- EXISTS -----------
# Есть ли студенты на курсах(привязаны ли)
SELECT * FROM public.courses c 
WHERE EXISTS (
    SELECT * FROM public.students s 
    WHERE s.course_id = c.id
)

# ------- NOT EXISTS -------
# Вытащить курсы в которых нету студентов
SELECT * FROM public.courses c 
WHERE NOT EXISTS (
    SELECT * FROM public.students s 
    WHERE s.course_id = c.id
)

# ================== CTE ===================
CTE - временная таблица которая существует только во время выполнения запроса
создается с помощью команды WITH

# Синтаксис
WITH <table_name_of_cte> AS (
    SELECT .....
)
SELECT * FROM <table_name_of_cte>

# Пример
# Найти дорогие курсы
WITH expensive_courses AS (
    SELECT * FROM courses
    WHERE price > 15000
)
SELECT * FROM expensive_courses

# CTE + JOIN
WITH expensive_courses AS (
    SELECT * FROM courses
    WHERE price > 15000
)

SELECT s.first_name, e_c.course_name
FROM public.students s
INNER JOIN expensive_courses e_c
ON s.course_id = e_c.id

# Несколько CTE
# Создаем несколько временных таблиц
WITH expensive_courses AS (
    SELECT * FROM courses
    WHERE price > 15000
),
hight_salary_teachers AS(
    SELECT * FROM teachers
    WHERE salary > 40000
)
SELECT c.course_name, h_s_t.first_name
FROM expensive_courses c
INNER JOIN hight_salary_teachers h_s_t
ON c.teacher_id = h_s_t.id


# =========== Практика =================
# Используя подзапросы
-- 1) Найти самый дешевый курс
-- 2) Самого высокооплачиваемого препода
-- 3) студента курса SQL

SELECT * FROM public.courses
WHERE price = (
    SELECT MIN(price)
    FROM public.courses
)

SELECT * FROM public.teachers
WHERE salary = (
    SELECT MAX(salary) FROM public.teachers
)

SELECT * FROM public.students
WHERE course_id = (
    SELECT id FROM public.courses
    WHERE course_name = 'SQL'
)


# Создать два CTE
# expensive_courses - выше 15000
# adult_students - старше 21
-- Соединить их и вывести
-- ИМЯ студента
-- возраст
-- названия курса
-- стоимость курса


WITH expensive_courses AS (
    SELECT id, course_name, price FROM courses
    WHERE price > 15000
),
adult_students AS (
    SELECT first_name, age, course_id FROM students
    WHERE age > 21
)
SELECT * FROM expensive_courses
INNER JOIN adult_students
ON adult_students.course_id = expensive_courses.id