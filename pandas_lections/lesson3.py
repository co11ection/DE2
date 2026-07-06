import pandas as pd
sales = {
"Менеджер": [
"Анна",
"Анна",
 "Иван",
 "Иван",
 "Мария",
 "Мария",
 "Мария"
],
"Город": [
 "Алматы",
 "Алматы",
 "Бишкек",
 "Бишкек",
 "Алматы",
 "Ташкент",
 "Алматы"
],
"Товар": [
 "Ноутбук",
 "Мышь",
 "Монитор",
 "Клавиатура",
 "Ноутбук",
 "Мышь",
 "Монитор"
],
"Количество": [
 2,
 10,
 3,
 6,
 1,
 15,
 4
],
"Цена": [
 65000,
 1500,
 40000,
 3500,
 65000,
 1500,
 40000
]
}

df = pd.DataFrame(sales)


# Группировка данных groupby
print(df.groupby("Менеджер").count())


# Подсчет колличества
print(df.groupby("Менеджер")["Количество"].sum())

# Среднее значение
print(df.groupby("Менеджер")["Цена"].mean())

# Максимум
print(df.groupby("Менеджер")["Цена"].max())
print(df.groupby("Менеджер")["Количество"].max())


# Минимум
print(df.groupby("Менеджер")["Цена"].min())
print(df.groupby("Менеджер")["Количество"].min())


# Группировка по двум столбцам
print(df.groupby(["Менеджер", "Город"])["Количество"].sum())

# Практика
# Общую сумму коллиства товаров по каждому городу
# Средняя цена по каждому городу
# Показать по каждому менеджеру и товару  продажи

print(df.groupby("Город")["Количество"].sum())
print(df.groupby("Город")["Цена"].mean())
print(df.groupby(["Менеджер", "Товар"])["Количество"].sum())


# Агрегирование agg()

result = df.groupby("Менеджер")["Количество"].agg(
    ["sum", "mean", 'max', 'min']
)
print(result)

# Несколько столбцов
result = df.groupby("Менеджер").agg(
    {
        "Количество": "sum",
        "Цена": "mean"
    }
)
print(result)

# Несколько функций
result = df.groupby("Менеджер").agg(
    {
        "Количество": ['sum', 'max'],
        "Цена": ["mean", 'min']
    }
)
print(result)


# Практика
# Сумму колличества
# максимальную цену
# минимальную цену

result = df.groupby("Менеджер").agg(
    {
        "Количество": "sum",
        "Цена": ['max', 'min']
    }
)

print(result)


# ------ Обьединение таблиц --------
# Таблица товаров
products = pd.DataFrame(
    {
        "id": [1, 2, 3, 4],
        "Товар": ["Ноутбук","Мышь","Монитор", "Клавиатура"]
    }
)

# Таблица заказов
order = pd.DataFrame(
    {
        "id": [1, 2, 3, 5],
        "Количество":[5, 20, 8, 5]
    }
)

# merge()
result = pd.merge(products, order, on="id")
print(result)



# Виды обьединений
# LEFT JOIN
result = pd.merge(
    products,
    order,
    on="id",
    how="left"
)
print(result)

# RIGHT JOIN
result = pd.merge(
    products,
    order,
    on="id",
    how="right"
)
print(result)

# OUTER JOIN
result = pd.merge(
    products,
    order,
    on='id',
    how="outer"
)
print(result)

# Практика
# Создать таблицу сотрудников и таблицу отделов и 
# обьединить(department_id)(left join, outer join)

employees = pd.DataFrame(
    {
        "name": ["Asan", "Asyl", "John", "Snow"],
        "department_id": [1, 2, 3, 4]
    }
)

department = pd.DataFrame(
    {
        "name": ['DE', "DS", "DA", "HR"],
        "department_id": [1, 2, 3, 5]
    }
)

print(pd.merge(
    employees, department, on="department_id", how="left"
))

print(pd.merge(
    employees, department, on="department_id", how="outer"
))

# Обьединение
employees1 = pd.DataFrame(
    {
        "name": ["Asan", "Asyl", "John", "Snow"],
    }
)

employees2 = pd.DataFrame(
    {
        "name": ["Aktan", "Aman", "Almaz", "Jane"],
    }
)
# cancat()
result = pd.concat([employees1, employees2])
print(result)

#Игнорирование старых индексов
result = pd.concat([employees1, employees2], ignore_index=True)
print(result)