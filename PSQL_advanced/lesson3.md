# ======= WINDOW fuctions - сложные запросы ------
1) Фреймы - "окно внутри окна" для каждой строки можно указать какие именно соседние строки будут участвовать в расчете

# Синтаксис:
    <функция>() OVER(
        [PARTITION BY ....]
        ORDER BY ....
        ROWS BETWEE <начало> AND <конец>
    )


# Накопительная сумма
SELECT month, revenue,
SUM(revenue) OVER(
    ORDER BY month
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS total
FROM monthly_sales;

# Скользящее среднее 
SELECT month, revenue,
AVG(revenue) OVER(
    ORDER BY month
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
) AS moving_avg
FROM monthly_sales

# ROWS - считает строго по количеству физических строк(2 строки назад, не зависимо от значений)

# RANGE - Группирует строки с одинаковыми значениями и после проводит ORDER BY  приводя в одну пиковую группу


# Суммировать продажи от начала до нынешней строки после отфильтровать по месяцам и вытащить с марта 2025-03-01
SELECT month, revenue,
SUM(revenue) OVER(
    ORDER BY month
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS total
FROM monthly_sales
WHERE month >= '2025-03-01';



# FIRST VALUE
SELECT course_name, teacher_id, price,
FIRST_VALUE(price) OVER(
    PARTITION BY teacher_id ORDER BY price
) AS min_price_for_teacher
FROM courses

# LAST VALUE
SELECT course_name, teacher_id, price,
LAST_VALUE(price) OVER (
    PARTITION BY teacher_id ORDER BY price
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS max_price_for_teacher
FROM courses


# NTILE - разбиение данных на равные группы
SELECT course_name, price,
NTILE(2) OVER (ORDER BY price) AS price_bucket
FROM courses


# NTH_VALUE - N-ое значение
SELECT course_name, teacher_id, price,
NTH_VALUE(price, 2) OVER (
    PARTITION BY teacher_id ORDER BY price
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS second_price_for_teacher
FROM courses;