# ================ Индексы и оптимизация ==========

['asan','aktan', 'almaz']
O(n) O(1) O(log n)

l m r
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] target = 9
l = 1. m=6 r=11
l = 6 m = 8 r = 11
l = 8 m=9 r = 11


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] target = 5
l = 1. m=6 r=11
l=1 m  m=3  r = 6
l =3  m = 4  r = 6
l = 4 m =5  r = 6

CREATE TABLE students_big(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    group_name VARCHAR(50),
    email VARCHAR(100)
)

# Генерация тестовых данных
INSERT INTO students_big(first_name, last_name, age, group_name, email)
SELECT 'Student' || i,
'Last'|| i,
18 + (i % 15),
'GROUP' || (i% 20),
'student' || i || '@gmail.com'
FROM generate_series(1, 500000) AS i;

ANALYSE students_big


EXPLAIN ANALYSE
SELECT * FROM students_big WHERE id = 250000




Индекс - это отдельная структура данных, которая хранит значение столбца в отсортированном виде с ссылкой на строку

Аналогия: Индексы - это содержание в начале книги

Для чего нужны индексы: Для быстрого поиска

# Синтаксис
    CREATE INDEX <название индекса> ON <название таблицы>(<название колонки>)


EXPLAIN ANALYSE
SELECT * FROM students_big WHERE group_name = 'GROUP5'

DROP INDEX idx_students_big_group_name;

CREATE INDEX idx_students_big_group_name ON students_big(group_name)

EXPLAIN ANALYSE
SELECT * FROM students_big WHERE group_name = 'GROUP5'


# Создать индекс на колонку age 
# просмотреть EXPLAIN ANALYSE до и после 

EXPLAIN ANALYSE
SELECT * FROM students_big WHERE age = 25

CREATE INDEX idx_students_big_age ON students_big(age)

EXPLAIN ANALYSE
SELECT * FROM students_big WHERE age = 25


# --------- Когда индексы не помогают, а наоборот вредят ------
1) Когда создается индексация на все колонки таблиц
2) Замедляет INSERT/UPDATE/DELETE
3) Занимает дополнительное место на диске(в памяти)
4) Нету смысла индексировать маленькие таблицы


# ---------- VACUUM и ANALIZE ------------
# Базовое обслуживание
--- Analize - обновляет статистику для планировщика запросов

--- VACUUM - убирает мертвые строки, оставшиеся после команд UPDATE/DELETE
бд не удаляет все сразу, а сохраняет кеши под капотом. что забивает память

VACUUM students_big

VACUUM ANALYSE students_big