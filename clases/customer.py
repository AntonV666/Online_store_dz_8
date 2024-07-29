class Customer:                                   
    '''                                          
    Класс Customer                             
    
    Этот класс представляет клиента интернет магазина.
    
    Метод __init__:
        Конструктор принимает список заказов клиента (orders) и инициализирует объект Customer с атрибутом name (имя клиента).
        Пример: customer_1 = Customer('Михаил', [order_1]) создаст клиента с именем 'Михаил' и списком [order_1].

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(customer_1) выведет Customer(name=Михаил, orders=[order_1]).
    '''
    def __init__(self, name: str, orders: str):    
        self.name = name                           
        self.orders = orders                       
        
    def __str__(self):                             
        return f'Клиент (Имя={self.name}, Список заказов={",".join([str(orders) for orders in self.orders])})'
