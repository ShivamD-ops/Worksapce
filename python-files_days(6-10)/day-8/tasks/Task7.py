class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_info(self):
        print(f"The product name is {self.name} \nThe price of product is {self.price}")

class Electronics(Product):
    def __init__(self,name,price,warrenty):
        Product.__init__(self,name,price)
        self.warrenty = warrenty
    def get_info(self):
        print(f'''
            Product name is -> {self.name}
            Product price is -> {self.price}
            Product warrenty is -> {self.warrenty}
        ''')

class Clothing(Product):
    def __init__(self,name,price,size):
        Product.__init__(self,name,price)
        self.size = size
    def get_info(self):
        print(f'''
            Product name is -> {self.name}
            Product price is -> {self.price}
            Product size is -> {self.size}
        ''')


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
                del self.__cart[product_name]
            else:
                self.__cart[product_name] -=1
            self.__total -= self.__product_map[product_name]

            print(f"Removed {product_name} from the cart")

    def total_price(self):
        return self.__total


prod1 = Electronics("ABC",800.0,"12 months")
prod2 = Clothing("DEF",900.0,"Medium")
prod3 = Electronics("GHI",799.0, "1 year")
prod4 = Electronics("PQR",9800.0,"12 months")
prod5 = Clothing("TUV",1900.0,"Large")
prod6 = Electronics("XYZ",7999.0, "3 year")
prod1.get_info()
prod2.get_info()

prod3.get_info()
prod4.get_info()

prod5.get_info()
prod6.get_info()

cart1 = ShoppingCart()
cart1.add_product(prod1)
cart1.add_product(prod2)
cart1.add_product(prod3)
cart1.add_product(prod4)
print(f"Current total value of cart is {cart1.total_price()}")
cart1.add_product(prod3)
print(f"Current total value of cart is {cart1.total_price()}")
cart1.remove_product("ABC")
print(f"Current total value of cart is {cart1.total_price()}")

'''
Question-1->
Redudency of code is reduced as we dont need to write again
the initialization of name and price

as get info of product class is overridden by 
get info of Electronic and Clothing class
'''
