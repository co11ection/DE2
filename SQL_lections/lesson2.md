# ============ CRUD ==================
# Создание таблиц
# Синтаксис
    CREATE TABLE <name of table> (
        <name column> <data type(тип данных)>, <ограничения>,
        .....
    )

# Пример
    CREATE TABLE courses(
    id INT PRIMARY KEY ,
    course_name VARCHAR(100),
    teacher VARCHAR(100),
    duration INT,
    price DECIMAL(10,2)
);

# INSERT - Создание данных
# Синтаксис
INSERT INTO <name of table>(column_name1, column_name2 ..)
VALUES (value1, value2 ...);
# Пример
    INSERT INTO courses(
    id, course_name, teacher, duration, price
    )
    VALUES (1, 'DE', 'Asan', 4, 20000);

# Несколько данных:
    INSERT INTO courses(
    id, course_name, teacher, duration, price
    )
    VALUES (2, 'DA', 'Almaz', 3, 25000),
    (3, 'SQL', 'Aidai', 4, 23000)

# SELECT - Получить записи(данные)
# Синтаксис
    SELECT *(все данные)/column _name1, column_name2 FROM <table_name>;
# Пример вывести все:
    SELECT * FROM courses;
# вывести по колонкам
    SELECT course_name, teacher, price FROM courses;
# Псевдонимы:
    SELECT 
    course_name AS "Курсы",
    teacher AS "Ментора", 
    price AS "Цена" 
    FROM courses;

# UPDATE - обновление(изменение) данных
# ПЕРЕД ОБНОВЛЕНИЕМ(ИЗМЕНЕНИЕМ) ОБЯЗАТЕЛЬНО ПРОСМОТРЕТЬ ДАННЫЕ ЧЕРЕЗ SELECT
# Синтаксис
    UPDATE <table_name>
    SET <column_name> = <value>
    WHERE <column_name> = <target>

# Пример
    UPDATE courses
    SET duration = 4
    WHERE id = 3;

    UPDATE courses
    SET course_name = 'DS'
    WHERE id = 1;

# DELETE - удаление данных 
# ПЕРЕД УДАЛЕНИЕМ ОБЯЗАТЕЛЬНО ПРОСМОТРЕТЬ ДАННЫЕ ЧЕРЕЗ SELECT

# Синтаксис
    DELETE FROM <table_name>
    WHERE <column_name> = <target>;
# Пример
    DELETE FROM courses
    WHERE id = 3;

# Удаление нескольких данных:
    DELETE FROM courses
    WHERE id IN (2, 4);


# ============ Практика =============
Создать таблицу students
поля: id, first_name, last_name, age, group_name
Добавить 5 студентов
и вывести всех студентов

CREATE TABLE students(
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    group_name VARCHAR(50)
);


INSERT INTO students (id, first_name, last_name, group_name, age)
VALUES (1, 'Adilet', 'Adiletov', 'DE2', 27),
(2, 'Nikita', 'Grebnev', 'DA', 20),
(3, 'Danya', 'Losev', 'DE2', 20),
(4, 'Almaz', 'Asanov', 'SQL', 30),
(5, 'Timurlan', 'Zhoroev', 'Python', 23);


SELECT * FROM students;