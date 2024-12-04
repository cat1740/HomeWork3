class Product:
    name = None
    price = None
    availability = None

    def __init__(self, name="Zero", price=0, availability=False):
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return "name: " + str(self.name) + ", price: " + str(self.price) + ", availability: " + str(self.availability)