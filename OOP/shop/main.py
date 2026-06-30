# CRUD - обривиатура
# CREATE - создать
# READ - Просмотреть
# UPDATE - обновить\изменить
# DELETE - удалить

# Наш проект
# Товар: Цена, Название, колличество, категория

# Пример: Ноутбук 8000$ 6 штук Электроника

# main.py, models.py, store.py


from abc import ABC, abstractmethod

class ProductBase(ABC):
    @abstractmethod
    def info(self):
        pass
    

class Product(ProductBase):
    def __init__(self, name: str, price: float, quantity: int, category: str):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__category = category
    
    # ---------- Getters methods ---------
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_category(self):
        return self.__category
    
    def get_quantity(self):
        return self.__quantity
    
    # ---------- setters methods --------
    def set_name(self, name):
        self.__name = name
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Цена должна быть больше 0!")
    
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Колличество не может быть отрицательным")
    
    def set_category(self, category):
        self.__category = category
    
    # ----------------------------------------
    def info(self):
        print(f""" 
            Название: {self.__name},
            Цена: {self.__price},
            Колличество: {self.__quantity},
            Категория: {self.__category}
        """)


class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity, "Еда")
        self.expiration_date = expiration_date
        
    def info(self):
        print(f"""
            Продукт питания
            
            Название: {self.get_name()}
            Цена: {self.get_price()}
            Колличество: {self.get_quantity()}  
            Срок годности: {self.expiration_date}
            """
        )

# Создать класс ElectronicProduct и добавить новый атрибут гарантия(warranty)
# создать обьект и проверить

class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity, "Электроника")
        self.warranty = warranty
        
    def info(self):
        print(f"""
            Электроника
            
            Название: {self.get_name()}
            Цена: {self.get_price()}
            Колличество: {self.get_quantity()}
            Гарантия: {self.warranty}
        """
        )

class Store:
    def __init__(self):
        self.products = []
        
    # ----- create -----
    def create_product(self, product):
        self.products.append(product)
        print("Товар добавлен в базу!")
        
    # -------read ---------
    def show_products(self):
        if not self.products:
            print("Товаров нету")
            return
        print("==== Список продуктов ===")
        for product in self.products:
            product.info()
            
    
    #-------- search ------
    def find_product(self, name):
        for product in self.products:
            if product.get_name().lower() == name.lower():
                return product
        return None  
            
    def search(self):
        name = input("Введите название: ")
        
        product = self.find_product(name)
        
        if product:
            product.info()
        else:
            print("Товар не найден")
            
            
            
            
            
            
            
            
            
            
store = Store()
store.create_product(
    ElectronicProduct(
        name="Ноутбук",
        price=38000,
        quantity=10,
        warranty='2 года'
    )
)
bread = FoodProduct(
    name="Белый хлеб",
    price=30,
    quantity=200,
    expiration_date="3 сутки"
)
store.create_product(bread)
store.show_products()

print('!!!!!!!!!!!!!!!!!!!!!!!')
store.search()