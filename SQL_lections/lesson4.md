# =============== Constraints(ограничения) =============
id price
1  -5000

# Основные ограничения
PRIMARY KEY - уникальный идентификатор
NOT NULL - Поле обязательное к заполнению
UNIQUE - Значение должно быть уникальным
DEFAULT - Значение по умолчанию
CHECK - Проверка условия
FOREIGN KEY - Связь между таблицами

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    age INT CHECK(age>=16) NOT NULL,
    course_id INT,
    FOREIGN KEY(course_id)
    REFERENCES courses(id)
);


CREATE TABLE teachers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    salary DECIMAL(10,2) CHECK(salary>0) NOT NULL
)


CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) CHECK(price>=0) NOT NULL,
    duration INT NOT NULL,
    teacher_id INT,
    FOREIGN KEY(teacher_id)
    REFERENCES teachers(id)
);

INSERT INTO public.teachers (first_name, email, salary)
VALUES
('Adil', 'adil@gmail.com', 70000),
('Umar', 'umar@gmail.com', 45000),
('Asan', 'asan@gmail.com', 60000)

SELECT * FROM public.teachers


-- 'DE' - Nikita
-- 'DS' - UMAR
-- 'Python' - Asan
-- 'SQL'

INSERT INTO public.courses (course_name, price, duration, teacher_id)
VALUES ('DE', 30000, 5, 4),
('DS', 20000, 8, 7),
('Python', 10000, 2, 8),
('SQL', 15000, 3, NULL);

SELECT * FROM public.courses


INSERT INTO public.students (first_name, age, last_name, course_id)
VALUES ('Asyl', 23, NULL, 1),
('Aktan', 25, 'Aktanov', 1),
('John', 23, 'Smit', 2),
('Gulchapchap', 26, 'Shypyrgul', 2),
('Adel', 20, 'Asanova', 1),
('Sabina', 21, 'Almazova', 2)

SELECT * FROM public.students


# =============== JOIN ==================
СОЕДИНЕНИЕ ТАБЛИЦ

# ------------ INNER JOIN ---------------
# Берутся все све связанные данные с обоих таблиц
SELECT students.first_name,
courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.id

SELECT * FROM students
INNER JOIN courses
ON students.course_id = courses.id

# JOIN с псевдонимомами
SELECT s.first_name, c.course_name
FROM public.students s
INNER JOIN public.courses c 
ON s.course_id = c.id

# =============== LEFT JOIN =================
# Все данные из левой таблицы 
# Связанные данные с правой таблицы
SELECT * FROM public.teachers t
LEFT JOIN public.courses c
ON t.id = c.teacher_id

# ============== RIGHT JOIN ================
# Все данные из правой таблицы
# Связанные данные с левой таблицы
SELECT * FROM public.teachers t
RIGHT JOIN public.courses c
ON t.id = c.teacher_id


# ============ UNION/UNION ALL ==========
# UNION - обьединение двух запросов (удаляет дубликаты)
SELECT t.first_name
FROM public.teachers t

UNION

SELECT s.first_name
FROM public.students s


# UNION ALL - обьединение двух запросов (не удаляет дубликаты)
SELECT t.first_name
FROM public.teachers t

UNION ALL

SELECT s.first_name
FROM public.students s



#   ПРАВИЛА UNION
КОЛИЧЕСТВО СТОЛБЦОВ ДОЛЖНО СОВПДАТЬ
