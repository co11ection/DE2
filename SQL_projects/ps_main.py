# Подключение к бд PostgreSQL

import psycopg2

# Создаем соединение
conn = psycopg2.connect(
    host="localhost",
    database="courses",
    user="macbook",
    password='1'
)

print("Соединение прошло успешно!", conn)

# Connection - соединение между Python и PostgreSQL

# Для выполнения SQL запросов нужен cursor

cursor = conn.cursor()

# Получить всех студентов
cursor.execute(
    """ 
    SELECT * FROM students
    """
)

students = cursor.fetchall()

for student in students:
    print(student)
    

# INSERT - создать

# cursor.execute(
#     """ 
#     INSERT INTO students (first_name, last_name, age, course_id)
#     VALUES ('Ali', 'Aliev', 20, 1)
#     """
# )
# conn.commit()

# UPDATE - изменение
# cursor.execute(
#     """ 
#     UPDATE students SET age=25 WHERE id=1
#     """
# )
# conn.commit()

# DELETE - Удаление
# cursor.execute(
#     """
#     DELETE FROM students WHERE id=1 
#     """
# )
# conn.commit()

# name = input("введите имя: ")
name = 'Asan'

cursor.execute(f"""
    SELECT * FROM students WHERE first_name='{name}'
""")
student = cursor.fetchall()
print(student)

cursor.close()
conn.close()