from Product import Product

class Cart:

    products = []
    cartsName = None

    def __init__(self, name):
        self.cartsName = name

    def addProduct(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            print("Error add product")

    def dellProduct(self, product):
        if isinstance(product, Product):
            self.products.remove(product)
        else:
            print("Error dell product")

    def getCheck(self):
        result = 0
        for i in self.products:
            result = result + i.price
        return result


    def __str__(self):
        result = 'Cart: '+ self.cartsName
        for i in self.products:
            result = result + "\n"+ str(i)
        return result