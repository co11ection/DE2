#=========== Pandas: Series, Dataframe, чтение csv и json ======
import pandas as pd

# lis1 = [1, 2, 3, 4, 5]
# print(lis1[10])

# dict1 = {
#     "name": "Asan",
#     "age": 25
# }

# print(dict1['age'])

products = [
    {
        "name": "Asus",
        "price": 38000,
        'quantity': 12
    },
    {
        "name": "Белый хлеб",
        "price": 30,
        "quantity": 200
    }
]
# for product in products:
#     print(product['name'])

# Pandas - библиотека Python для анализа и обработки табличных данных


# [
#     ['name'],['price'],['quantity'],
#     ['Asus'],[38000],[20]
# ]

# ======= Series ========
# одномерная структура данных

# Создание
numbers = pd.Series([10, 20, 30, 40])
print(numbers)

cities = [
    "Бишкек", "Алматы", "Ташкент"
]

cities_series = pd.Series(
    cities,
    index=["KG", "KZ", "UZ"]
)
print(cities_series)

list1 = [5, 10, 15, 20] #-  создать Series

list2 = pd.Series(list1)
print(list2)

# DataFrame - двумерная таблица\массив

data = {
    "Имя": ["Асан", "Никита", "Актан"],
    "Возраст": [20, 25, 24],
    "Город": ["Бишкек", "Амстердам", "Москва"]
}
df = pd.DataFrame(data)
print(df)

# Получение столбца
print(df["Имя"])

# Несколько столбцов
print(df[["Имя", 'Город', "Возраст"]])

# Размерность
print(df.shape)

# Название столбцов
print(df.columns)

# Индексы
print(df.index)

# Типы данных
print(df.dtypes)

# Общая информация
print(df.info())


# Статистика
print(df.describe())


# Первые строки
print(df.head(2))


# Последние строки
print(df.tail(2))


# Создать таблицу
# Поля;
# Имя
# Зарплата
# Отдел

# Вывести первые строки
# Список столбцов
# Информация о таблице
# Размерность
# Вывести последние строки
# Вывести статистику

table = {
    "Имя": ['Asan', "Umar", "Nikita", "Sultan"],
    "Зарплата": [20000, 15000, 60000, 70000],
    "Отдел": ["DS", "DA", "DE", "DA"]
}

df = pd.DataFrame(table)
print(df.head(2))
print(df.columns)
print(df.info())
print(df.shape)
print(df.tail(2))
print(df.describe())


# ======= Чтение CSV ==========
# CSV - самый распространенный формат файла 
# для хранений табличных данных в программирование

# df = pd.read_csv("students.csv", sep=";")
# print(df)

# print(df.head(2))
# print(df.info())


# ========= Чтение json файлов ======
# JSON - Формат файла\обьекта для передачи 
# данных между язфками программирования

df = pd.read_json('students.json')
print(df)