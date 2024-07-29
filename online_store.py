# Интернет-магазин с системой скидок и учётом заказов

''' Создайте систему для интернет-магазина, которая включает следующие функциональные возможности:
1.	Классы Product, Customer, Order и Discount:
o	Product - класс, представляющий товар, с атрибутами name (название товара) и price (цена товара).
o	Customer - класс, представляющий клиента, с атрибутами name (имя клиента) и orders (список заказов клиента).
o	Order - класс, представляющий заказ, с атрибутом products (список товаров в заказе).
o	Discount - класс для применения скидок, с атрибутами description (описание скидки) и discount_percent (процент скидки).
2.	Методы класса и статические методы:
o	Используйте статические методы в классе Discount для расчета цены со скидкой и применения различных видов скидок 
(например, сезонная скидка, скидка по промокоду и т.д.).
o	Используйте методы класса в классе Order для подсчета общего количества заказов и общей суммы заказов для всех клиентов.
3.	Дандер методы:
o	Реализуйте дандер методы __str__ и __repr__ для всех классов, чтобы выводить удобочитаемую информацию о клиентах, 
аказах и продуктах.
o	Реализуйте дандер методы __eq__ и __lt__ в классе Product для сравнения товаров по цене.
Требования к реализации:
1.	Создайте несколько продуктов и клиентов.
2.	Реализуйте функциональность для добавления заказов к клиентам.
3.	Примените различные виды скидок к заказам.
4.	Подсчитайте общее количество заказов и общую сумму всех заказов для всех клиентов.
5.	Выведите информацию о клиентах, заказах и продуктах с использованием дандер методов.
Домашнее задание сдается отдельным GitHub репозиторием, в котором должен быть только код домашнего задания и изображение 
с показом запуска (вывода в консоль) и время, когда сделано изображение!!!
'''

# Загружаем классы
from clases.product import Product
from clases.customer import Customer
from clases.order import Order
from clases.discount import Discount

# Создаем продукты
product_1 = Product('Apple', 100)
product_2 = Product('Samsung', 30)
product_3 = Product('Xiaomi', 10)

# Выводим информацию о продуктах
print(product_1)   
print(product_2)     
print(product_3)    

# Создаем различные виды скидок
discount_1 = Discount('Промокод', 15)
discount_2 = Discount('Сезон', 10)
discount_3 = Discount('Новый Год', 5)   

# Выводим информацию о скидках
print(discount_1)   
print(discount_2) 
print(discount_3) 

# Рассчитываем цены с учетом скидок
# discounted_price_1 = Discount.calculate_discounted_price(product_1.price, discount_1.discount_percent)
# discounted_price_2 = Discount.calculate_discounted_price(product_2.price, discount_2.discount_percent)
# discounted_price_3 = Discount.calculate_discounted_price(product_3.price, discount_3.discount_percent)

# Рассчитываем цены с учетом скидок
discounted_price_1 = product_1.get_discounted_price(discount_1.discount_percent)
discounted_price_2 = product_2.get_discounted_price(discount_2.discount_percent)
discounted_price_3 = product_3.get_discounted_price(discount_3.discount_percent)


# Выводим информацию о ценах со скидками
print(f"Сниженная цена на {product_1.name} с учетом скидки {discount_1.description} составляет: {discounted_price_1}")
print(f"Сниженная цена на {product_2.name} с учетом скидки {discount_2.description} составляет: {discounted_price_2}") 
print(f"Сниженная цена на {product_3.name} с учетом скидки {discount_3.description} составляет: {discounted_price_3}")   

# Создаем заказы
order_1 = Order([product_1])
order_2 = Order([product_1, product_2])
order_3 = Order([product_1, product_2, product_3])

# Выводим список заказов без скидки
print(order_1)
print(order_2)
print(order_3)

# Выводим общую цену заказов с учетом скидок
print('Общая цена заказа с учетом скидки составляет: ', order_1.get_total_price(discount_1.discount_percent))
print('Общая цена заказа с учетом скидки составляет: ', order_2.get_total_price(discount_2.discount_percent))
print('Общая цена заказа с учетом скидки составляет: ', order_3.get_total_price(discount_3.discount_percent))

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")

# Выводим общую сумму заказов
total_price = Order.total_price()  # получаем общую стоимость заказа
print(f'Общая сумма заказов: ', (total_price))

# Создаем покупателей
customer_1 = Customer('Михаил', [order_1])
customer_2 = Customer('Антон', [order_1, order_2])
customer_3 = Customer('Даша', [order_1, order_2, order_3])

# Выводим информацию о покупателях
print(customer_1)
print(customer_2)
print(customer_3)