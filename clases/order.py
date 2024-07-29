class Order:                                   
    """
    Класс Order

    Этот класс представляет заказ в интернет-магазине.
    
    Атрибут класса _total_orders:
        Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.
        
    Атрибут класса _total_price:
        Счетчик общей суммы созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.

    Метод __init__:
        Конструктор принимает список товаров (products) и инициализирует объект Order.
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order_1 = Order([product_1]) создаст заказ, содержащий один товар (product_1).
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order_1 = Order([product_1]) создаст заказ, содержащий один товар (product_1).
        
    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.
        
    Метод total_price:
        Метод класса, который возвращает общую сумму созданных заказов.
        Пример: Order.total_price() вернет общую сумму созданных заказов.
    
    Метод __get_total_price__ возвращает общую сумму заказа с учетом скидки
        
    Метод __str__:
        Возвращает список товаров в заказе.
        Пример: print(order1) выведет Order([product_1]).
    """
    
    _total_orders = 0                             
    _total_price = 0                              

    def __init__(self, products):                 
        self.products = products                  
        Order._total_orders += 1                   
        for product in products:
            Order._total_price += product.price                  
                
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    @classmethod
    def total_price(cls):
        return cls._total_price
    
    def get_total_price(self, discount_percent):
        total_price = sum([product.get_discounted_price(discount_percent) for product in self.products])
        return total_price
        
    def __str__(self):
        return f'Заказ (Список заказов={",".join([str(product) for product in self.products])})'  