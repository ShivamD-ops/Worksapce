class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def info(self):
        print(f'Title = {self.title}\nAuthor = {self.author} \nprice = {self.price}')

new_book = Book("Harry Potter Prisoner of Askaban", "JK Rolling",290.0)
new_book.info()

# We can modify the Book class by adding price as a parametre 
# to be passed by while creating a new object
# and updating the __init__ constructor to initioalize it
