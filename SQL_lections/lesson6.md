# ==================== CROSS JOIN ===========
Нужен чтобы получить все возможные комбинации

students            courses
adil                DE  
asan                DS
aktan               DA


adil                DE
adil                DS
adil                DA
asan                DE
asan                DS
asan                DA
aktan               DE
aktan               DA
aktan               DS

# Синтаксис
    SELECT */column_names FROM table_name1
    CROSS JOIN table_name2

# Пример
    SELECT * FROM public.students
    CROSS JOIN public.courses

# Получить все возможные комбинации между таблицой преподавателей и курсов
SELECT t.first_name, c.course_name FROM public.teachers t
CROSS JOIN public.courses c


# ============== SELF JOIN ===================
# Соединение таблицы сама с собой

# Создание таблицы которая ссылается сама на себя
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    manager_id INT,
    FOREIGN KEY(manager_id)
    REFERENCES employees(id)
)


INSERT INTO public.employees (name, manager_id)
VALUES ('Erhan', NULL),
('Bermet', 1),
('Sher', 1),
('Nurzhan', 2),
('Emir', 3)


SELECT * FROM public.employees

Employee
('Erhan', NULL), 1
('Bermet', 1), 2
('Sher', 1), 3
('Nurzhan', 2), 4
('Emir', 3) 5


Manager
('Erhan', NULL), 1
('Bermet', 1),  2
('Sher', 1),    3
('Nurzhan', 2), 4
('Emir', 3) 5
# ПРИМЕР
    SELECT employe.name, manager.name AS manager_name
    FROM public.employees employe
    LEFT JOIN public.employees manager
    ON employe.manager_id = manager.id

# ----------------- UPDATE с JOIN ---------------
# Синтаксис
    UPDATE ...... FROM  ....

# Пример
# Надо увеличить цену курсов на 10% у препода Nikita
    UPDATE public.courses c
    SET price = price * 1.1
    FROM public.teachers t
    WHERE c.teacher_id = t.id
    AND t.first_name = 'Nikita'


# -------- DELETE c JOIN -------------
в PostgreSQL используется для таких моментов: USING

# Удалить курсы преподователя Umar

DELETE FROM public.courses c
USING teachers t
WHERE c.teacher_id = t.id
AND t.first_name = 'Umar';

SELECT * FROM public.courses

DELETE FROM students s
USING courses c
WHERE s.course_id = c.id
AND c.course_name = 'DS'

SELECT * FROM public.students
INNER JOIN public.courses
ON students.course_id = courses.id


# ============= Рекурсия =================
Это когда обьект обращается сама к себе
В программирование когда функция вызывает сама себя

<!-- WITH RECURSIVE -->
# Синтаксис
WITH RECURSIVE name AS(
    Начальный запрос
    UNION ALL
    рекурсивный запрос
)
SELECT * FROM name


WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n+1
    FROM numbers
    WHERE n < 10
)
SELECT * FROM numbers


# Получить уровни оргонизации