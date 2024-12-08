class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(f"product with name {self.name} created of price {self.price}")
class ShoppingCart:

    def __init__(self):
        self.__cart = {}
        self.__product_map = {}
        self.__total = 0

    def add_product(self,product):
        if self.__cart.get(product.name):
            self.__cart[product.name] += 1
        else:
            self.__cart[product.name] = 1
        self.__total += product.price
        self.__product_map[product.name] = product.price
        print(f"Added {product.name} of price: {product.price} to the cart")

    def remove_product(self,product_name):
        # del self.cart[product_name]]
       
        if self.__cart[product_name] >= 1:
            if self.__cart[product_name] == 1:
                del self.cart[product_name]
            else:
                self.__cart[product_name] -=1
            self.__total -= self.__product_map[product_name]

            print(f"Removed {product_name} from the cart")

    def total_price(self):
        return self.__total
prod1 = Product("ABC",800.0)
prod2 = Product("DEF",900.0)
prod3 = Product("GHI",799.0)
cart1 = ShoppingCart()
cart1.add_product(prod1)
cart1.add_product(prod1)
cart1.add_product(prod1)
cart1.add_product(prod2)
print(f"Current total value of cart is {cart1.total_price()}")
cart1.add_product(prod3)
print(f"Current total value of cart is {cart1.total_price()}")
cart1.remove_product("ABC")
print(f"Current total value of cart is {cart1.total_price()}")

'''
Shopping cart and Product have a relation that ShoppingCart has a method that accepts object of type 
Product.
This example is different from inheritence as we do not
inherit any of product's properties in the class ShoppingCart
instead we use the object of class Product just like we 
use objects of class created in main method.


We used dictionary with product name as key and quantity as value
to handle scenario where the same product is added multiple times
also created a product map dictionary to get price values
'''



