class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__is_borrowed = False
        print(f"new book found {title} by {author}")

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"Book {self.title} Borrowed Successfuly")
        else:
            print(f"Book {self.title} Already Borrowed")
        
    def return_book(self):
        self.__is_borrowed = False
        print(f"Book {self.title} Returned Suucessfuly")

class Library:
    def __init__(self):
        self.__books = []
        print(f"library created")
    
    def add_book(self,book):
        if book in self.__books:
            print(f"book {book.title} already in library")
        else:
            self.__books.append(book)
            print(f"book {book.title} added to library")
        # print(f"current list of books-> {self.__books}")
    def borrow_book(self,title):
        for i in self.__books:
            if i.title == title:
                i.borrow()
                break
        print(f"book {title} not present in library")
        # print(f"current list of books-> {self.__books}")
    def return_book(self,title):
        for i in self.__books:
            if i.title == title:
                i.return_book()
                break
        print(f"book {title} not present in library")
        # print(f"current list of books-> {self.__books}")
book1 = Book("ABC","abc")
book2 = Book("DEF","def")
book3 = Book("GHI","ghi")
book4 = Book("JKL","jkl")
book5 = Book("MNO","mno")
book6 = Book("PQR","pqr")

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)
library1.add_book(book6)

library1.borrow_book("ABC")
library1.borrow_book("DEF")
library1.return_book("ABC")
library1.borrow_book("ABC")
library1.borrow_book("GHI")
library1.borrow_book("ABC")
library1.borrow_book("JKL")

"""
Library Class manage the relationship b/w library and books by
accessin the methods of book class from itself and allowing
users to interect with library and encapsulation works here as
the library class encapsulates the functionality and 
functions like borrow_book(), return_book takes care of the rest
updating in book object of Book class

simple if check can help handle if book is already borrowed
if boolean is_borrowed is true
we can use both exception raise and print 
to if book is already borrowed.
"""
