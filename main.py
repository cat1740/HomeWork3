from Product import Product
from Cart import Cart

monitor = Product("Monitor", 200, True)
computer = Product("PC", 1000, True)
gamepad = Product("PlayStation 5", 650, True)

cart01 = Cart("Max")

cart01.addProduct(monitor)
cart01.addProduct(computer)
cart01.addProduct(gamepad)
print(cart01)
print()
cart01.dellProduct(computer)
print(cart01)
print()

money = cart01.getCheck()
print("Total amount: ", money)







