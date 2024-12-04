"""
1. Створити клас Cart
2. Визначити змінну типу list (products = [])
3. метод addProduct (додати товар) до products
4. метод __init__
5. метод __str__ (перелік всіх товарів (назва, ціна, наявність))
"""

class Cart:

    products = []





    def __str__(self):
        result = 'Cart\n'
        for i in self.products:
            result = result + "\n"+ str(i)
        return result