from Product import Product
from Cart import Cart

monitor = Product("Monitor", 200, True)
computer = Product("PC", 1000, True)
gamepad = Product("PlayStation 5", 650, True)

cart01 = Cart()
cart02 = Cart()
cart01.name = 'Cart01'

cart02.products.append(monitor)


print(cart01)





