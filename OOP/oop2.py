# ============== Принципы ООП ================
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация

# 1) Инкапсуляция - это сокрытие внутренних реализаций 
# обьекта (атрибуты\ методы) и предоставление доступа к данным

# Публичный - element = 12
# Защищенный - _element = 12
# Приватный - __element = 12

class BankAccount:
    def __init__(self, username: str, card_number: int, balance: float = 0):
        self.username = username
        self._card_number = card_number
        self.__balance = balance
    
    def info(self):
        print( f"""
              Пользователь: {self.username}
              Номер карты: {self._card_number}
              Баланс: {self.__balance}
            """  
        )
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        self.__balance += amount

aktans_account = BankAccount(username="aktan3000", card_number=4169585347477575)
aktans_account.info()
print(aktans_account.username)
# print(aktans_account.__balance) AttributeError: 'BankAccount' object has no attribute '__balance'
print(aktans_account._BankAccount__balance) # Обход защиты приватных атрибутов
print(aktans_account.get_balance())
aktans_account.deposit(10000.0)
print(aktans_account.get_balance())
aktans_account.info()

# Полиморфизм
print(5 + 5)
print("5" + "5")

class Dog:
    def speak(self):
        print("GAV GAV")
        
ovcharka = Dog()
ovcharka.speak()

class Cat:
    def speak(self):
        print("MEOW MEOW")

pifagor = Cat()
pifagor.speak()

# Абстракция - Правильная постройка классов
# (пользователь видет только главное, а все остальное в абстракции)
# и правильность полиморфизма

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


sq1 = Square(4)
print(sq1.area())

ci = Circle(10)
print(ci.area())


# Ассоциация - про связи
# Агрегация - слабая связь

class Motor:
    def start(self):
        print("Motor started")
        
e_100 = Motor()

class Car:
    def __init__(self, motor):
        self.motor = motor
        
    def start(self):
        self.motor.start()
        
nissan = Car(e_100)
nissan.start()

# Композиция - сильная связь
class Motor:
    def start(self):
        print("Motor started 2")

class Car:
    def __init__(self):
        self.motor = Motor()
        
    def start(self):
        self.motor.start()
        
nissan = Car()
nissan.start()


# SOLID