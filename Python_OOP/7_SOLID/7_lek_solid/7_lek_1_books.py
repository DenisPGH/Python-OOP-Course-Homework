"""Refactor the provided code, so there is a separate class called Library,
 which contains books and has a method called find_book(title) that returns the book with the given title.
  Remove the unnecessary code from the Book class."""
class Library:
    def __init__(self,name):
        self.name = name
        self.books=[] # store the books here


    def __find_book_by_name(self,name):
        for each in self.books:
            if each.title==name:
                return each

    def find_book(self,title):
        return self.__find_book_by_name(title)

    def add_book(self,book):
        self.books.append(book)






class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

l=Library("BookStore")

book= Book("Sleep","deni")

l.add_book(book)
print(l.find_book("Sleep"))
