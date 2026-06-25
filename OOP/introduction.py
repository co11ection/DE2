#================= OOP ============
# Обьектно ориентированное программирование - подход к разработке
# программ, которые состоят их обьектов

# данные(атрибуты)
# действие(методы)

# Автомобиль
# ---Атрибуты--
# колеса
# марка
# цвет
# двери
# ---- Методы ---
# ездить
# тормозить
# сигналить

# Основные понятия которые должны запомнить
# Класс - Шаблон обьекта
# Обьект - Экземляр класса
# Атрибут - Данные обьекта, переменные
# Метод - действия, функции

# Классы и обьекты
class CreateReadUpdateDelete:
    pass


class Student:
    def __init__(self, name, age): # Создание атрибутов(инициолизировать)
        # self - ссылка на обьект
        self.name = name
        self.age = age
    
    def say_hello(self):
        return "hello"
    
    def student_info(self):
        return f"name: {self.name}, age:{self.age}"

student1 = Student('Nurbek', 24)
print(student1.name)
print(student1.age)
print(student1.say_hello())
print(student1.student_info())


# Создать класс Dog - атрибуты name, breed
# Метод bark() - гав гав!

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        return "Гав гав!"
    
dog1 = Dog('barsik', 'ovcharka')
print(dog1.name)
print(dog1.bark())

dog2 = Dog('Sharik', 'dvorniajka')
print(dog2.name)
print(dog2.bark())


# Создать класс Book 
# Атрибуты - title, author
# Методы - show_info()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def show_info(self):
        return f"title: {self.title}, author: {self.author}"
    
book1 = Book("Самурай без меча", "Масохиро")
print(book1.show_info())



# ================ Принципы ООП ==================
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация

# Наследование - позволяет передавать от родительского 
# класса дочернему классу все его методы и атрибуты

class Animal:
    def __init__(self, legs):
        self.legs = legs
        
    def eat(self):
        return "Может кушать"
    
class Dog(Animal):
    def __init__(self, legs, nose):
        super().__init__(legs)
        self.nose = nose
    
    def bark(self):
        return 'gaf gaf'
    
    def eat(self):
        return 'кушает кость'
        
dog1 = Dog(4, 'black')
print(dog1.legs)
print(dog1.eat())
print(dog1.bark())


# Создать класс Transport - родительский класс с методом move()
# Создать дочерний класс Car который наследуется от Transport
# вывести через дочерний класс метод move()

class Transport:
    def move(self):
        return "Можно ездить"
    
class Car(Transport):
    pass

car1 = Car()
print(car1.move())



class Animal:
    def __init__(self, legs):
        self.legs = legs
        
    def eat(self):
        return "Может кушать"
    
class Dog(Animal):
    def __init__(self, legs, nose):
        super().__init__(legs)
        self.nose = nose
    
    def bark(self):
        return 'gaf gaf'
    
    def eat(self):
        return 'кушает кость'
    

class Cat(Animal):
    pass

cat1 = Cat(legs=4)
print(cat1.legs)
print(cat1.eat())

dog1 = Dog(4, 'black')
print(dog1.eat())
print(dog1.bark())