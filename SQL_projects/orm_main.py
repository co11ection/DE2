# ORM - Object Relational Mapping
# Идея: Таблица в БД превращается в класс Python

# Без ORM
# SELECT * FROM students

# С ORM
# Students.query.all()

# Создание подключение
from sqlalchemy import  *
from sqlalchemy.orm import *

engine = create_engine(
    "postgresql://macbook:1@localhost/courses"
)

# Базовый класс
Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

Session = sessionmaker(bind=engine)

session = Session()

# Получить данные(всех студентов)
students = session.query(Students).all()
for student in students:
    print({
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age
    })

# Получение одного студента
student = session.query(Students).first()

print(student.first_name)


# Добавить данные в таблицу
# new_student = Students(
#     first_name='Bakyt',
#     last_name='Bakytov',
#     age=20
# )
# session.add(new_student)
# session.commit()

# Фильтрация данных
student = session.query(Students).filter(Students.id == 2).first()

print(
    {
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age
    }
)
# Изменение данных в таблиц
student = session.query(Students).filter(Students.id == 2).first()
student.age = 27
session.commit()


# Удаление данных из таблицы
# student = session.query(Students).filter(Students.id == 11).first()
# session.delete(student)
# session.commit()


# Фильтрация по нескольким условиям
students = session.query(Students).filter(
    Students.age > 20,
    Students.first_name == "Asan"
).all()

for student in students:
    print(
    {
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age
    }
)