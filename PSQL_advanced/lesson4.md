# ======== Слои хранилища ================
# STAGING - сырая копия "без изменений как есть"
# ODS - (консолидация + легкая очистка)
# DDS - Нормализация + историчность, единая модель
# MART - денормализационные витрины под конкретные задачи(отчеты)

# Слой| что оно делает| структура данных
STAGING| копирует данные как есть| 1 в 1 похожа на структуру источника + те же поля
ODS| консолимдирует источники, производит легкую очистку| близка к источнику но немного причесано(убраны дубликаты, и форматы)
DDS| нормализация, сурогатные ключт, историчность| источник правды
MART| денормализация под конкретные отчеты| факты + измерение



# STAGING - добавляются новые поля по типу когда загружено ('_loaded_at")
# из какого источника('_source_system')
# либо TRUNCATE + INSERT либо INSERT

# Пример
    CREATE TABLE staging.stg_courses(
    id INT,
    course_name VARCHAR(100),
    price DECIMAL(10,2),
    duration INT,
    teacher_id INT,
    _loaded_at TIMESTAMP DEFAULT NOW(),
    _source_system VARCHAR(50) DEFAULT 'main_db'
)

INSERT INTO staging.stg_courses(id, course_name, price, duration, teacher_id)
SELECT id, course_name, price, duration, teacher_id
FROM public.courses

SELECT * FROM staging.stg_courses

# Полная перезагрузка
TRUNCATE TABLE staging.stg_courses


# teachers, students -> stg_teachers, stg_students
CREATE TABLE staging.stg_teachers(
    id INT,
    first_name VARCHAR(50),
    email VARCHAR(100),
    salary DECIMAL(10,2),
    _loaded_at TIMESTAMP DEFAULT NOW(),
    _source_system VARCHAR(50) DEFAULT 'main_db'
)

INSERT INTO staging.stg_teachers(id, first_name, email, salary)
SELECT id, first_name, email, salary
FROM public.teachers

SELECT * FROM staging.stg_teachers


CREATE TABLE staging.stg_students(
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    course_id INT,
    _loaded_at TIMESTAMP DEFAULT NOW(),
    _source_system VARCHAR(50) DEFAULT 'main_db'
)

INSERT INTO staging.stg_students(id, first_name, last_name, age, course_id)
SELECT id, first_name, last_name, age, course_id
FROM public.students

SELECT * FROM staging.stg_students

# ODS
# Здесь данные с staging (возможно из нескольких источников) обьединяются в единую структуру
# легкая очистка "TRIM" очистка пробелов, приведение регистра email, удаление дублей
# бизнес логика (расчеты или агрегации) здесь еще не до конца - она в следующих слоях

# Пример
# Очистка дедупликации courses
CREATE TABLE ods.ods_courses AS
SELECT DISTINCT ON (id)
id,
TRIM(course_name) AS course_name,
price,
duration,
teacher_id
FROM staging.stg_courses
ORDER BY id, _loaded_at DESC;

SELECT * FROM ods.ods_courses

# Очистка email
CREATE TABLE ods.ods_teachers AS
SELECT DISTINCT ON (id)
id,
TRIM(first_name) as first_name,
LOWER(TRIM(email)) as email,
salary
FROM staging.stg_teachers
ORDER BY id, _loaded_at DESC;

SELECT * FROM ods.ods_teachers


# построить новыую таблицу ods_students вытащить данные из stg_students

CREATE TABLE ods.ods_students AS
SELECT DISTINCT ON (id)
id,
TRIM(first_name) as first_name,
TRIM(last_name) as last_name,
age,
course_id
FROM staging.stg_students
ORDER BY id, _loaded_at DESC;

SELECT * FROM ods.ods_students

# DDS - детальный слой с историчностью
