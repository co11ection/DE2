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
    
    # --------- update -------------
    def update_product(self, name):
        product = self.find_product(name)
        if product:
            try:
                price = float(input("Новая цена: "))
                quantity = int(input("Новое количество: "))
                
                product.set_price(price)
                product.set_quantity(quantity)

            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            
            else:
                print("Товар успешно обновлен")
        else:
            print("Товар не найден")
            
    
    def delete_product(self, name):
        product = self.find_product(name)
        if product:
            self.products.remove(product)
            print("Товар удален")
        else:
            print("Товар не найден")
            
    # --------- sorting ---------
    def sort_price(self):
        sorted_products = sorted(
            self.products,
            key=lambda product: product.get_price() 
        )
        print("Сортировка по цене")
        for product in sorted_products:   
            product.info()
    
    def sort_name(self):
        sorted_products = sorted(
            self.products,
            key = lambda product: product.get_name().lower()
        )
        print("Сортировка по названию")
        for product in sorted_products:   
            product.info()

            
            
            
            
            
            
            
            
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
    name="белый хлеб",
    price=30,
    quantity=200,
    expiration_date="3 сутки"
)
store.create_product(bread)
store.show_products()

print('!!!!!!!!!!!!!!!!!!!!!!!')
# store.search()

# store.update_product("Ноутбук")
# print('удаление продукта')
# store.delete_product("ноутбук")
print('Список продуктов')
store.show_products()

# store.sort_price()
# store.sort_name()


while True:
    print(
        """
        ========================
                Магазин
        ========================
        1. Добавить товар
        2. Показать товары
        3. Изменить товар
        4. Удалить товар
        5. Поиск товара
        6. Сортировака товара по цене
        7. Сортировка товара по названию
        0. Выход
        """
    )
    choice = input("Выбери пункт: ")
    
    if choice == '1':
        print("1. Обычный товар")
        print("2. Продукт питания")
        print("3. Электроника")
        product_type = input("Тип товара: ")
        
        try:
            name = input("Название: ")
            price = float(input("Цена: "))
            quantity = int(input("Количество: "))
            
            if product_type == '1':
                category = input("Категория: ")
                
                product = Product(
                    name=name,
                    price=price,
                    quantity=quantity,
                    category=category
                )
            elif product_type == "2":
                expiration = input("Срок годности: ")
                
                product = FoodProduct(
                    name=name,
                    price=price,
                    quantity=quantity,
                    expiration_date=expiration
                )
            elif product_type == "3":
                warranty = input("Гарантия: ")
                
                product = ElectronicProduct(
                    name=name,
                    price=price,
                    quantity=quantity,
                    warranty=warranty
                )
            else:
                print("Не верный тип продукта")
                continue
            
            store.create_product(product)
        except ValueError:
               print("Ошибка ввода")
    
    elif choice == '2':
        store.show_products()
    elif choice == "3":
        name = input("Название товара: ")
        store.update_product(name)
    elif choice == '4':
        name = input("Название товара: ")
        store.delete_product(name)
    
    elif choice == '5':
        store.search()
    
    elif choice == "6":
        store.sort_price()
    
    elif choice == '7':
        store.sort_name()
    
    elif choice == "0":
        print("До свидания!")
        break
    
    else:
        print("Неверный пункт меню!!!")