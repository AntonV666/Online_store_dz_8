class Product:                                   
    '''                                          
    Класс Product                             
    
    Этот класс представляет товар в интернет магазине.
    
    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product_1 = Product('Apple', 100) создаст товар с названием 'Apple' и ценой 100.
        
    Метод __get_discounted_price__ возвращает цену с учетом скидки.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product_1) выведет Product(name=Apple, price=100).
    '''
    def __init__(self, name: str, price: float):    
        self.name = name                          
        self.price = price    
        
    def get_discounted_price(self, discount_percent):
        return self.price * (1 - discount_percent / 100)                   
        
    def __str__(self):                            
        return f'Продукт (Название={self.name}, Цена={self.price})'