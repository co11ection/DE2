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
        "first_name": student.first_name,
        "last_name": student.last_name
    })

# Получение одного студента
student = session.query(Students).first()

print(student.first_name)