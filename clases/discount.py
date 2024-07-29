class Discount:                                   
    '''                                          
    Класс Discount                             
    
    Этот класс для применения скидок в интернет магазине.
    
    Метод __init__:
        Конструктор инициализирует объект Discount с двумя атрибутами: description (описание скидки) и discount_percent (процент скидки).
        Пример: discount_1 = Discount('Промокод', 15) создаст скидку с названием 'Промокод' и размером 15 %.
        
    Метод calculate_discounted_price:
        Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
        Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(discount_1) выведет Discount(description=Промокод, discount_percent=15).
    '''
    def __init__(self, description: str, discount_percent: int):    
        self.description = description                              
        self.discount_percent = discount_percent     
    
    @staticmethod    
    def calculate_discounted_price(price, discount_percent):
        return price * (1 - discount_percent / 100)               
        
    def __str__(self):                         
        return f'Скидка (Описание={self.description}, Процент={self.discount_percent})'