"""In the library.py create a class project_. Upon initialization,
it will not receive anything, but it should have the following instance attributes:
 o	user_records - an empty list that will store the users (users objects) of the library
o	books_available - an empty dictionary that will keep information regarding the authors (key: str)
and the books available for each of the authors (list of strings)
o	rented_books - an empty dictionary that will keep information regarding the usernames (key: str)
and nested dictionary as a value in which will keep information regarding the book names (key: str)
 and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}).
"""




class Library():

    def __init__(self):
        self.user_records=[] #store the users (users objects)
        self.books_available={} #authors (key: str) and the books available for each of the authors (list of strings)
        self.rented_books={} # {usernames: {book names: days to return,a:2}}). key=username, value={ store key=book_name, value=days left before returning the book to the library (int)}



    def get_book(self,author: str, book_name: str, days_to_return: int, user):
        if book_name in self.books_available[author]:
            if user.username not in self.rented_books:
                self.rented_books[user.username]={} # add to history for return
            self.rented_books[user.username][book_name]= days_to_return
            #library.books_available[author]=[]
            self.books_available[author].remove(book_name) # remove from avaiable for this book
            user.books.append(book_name) # add for current user
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for each_user,books in self.rented_books.items():
            for book,day_for_return in books.items():
                if book_name ==book:
                    return f'The book "{book_name}" is already rented and will be' \
                           f' available in {day_for_return} days!'


    def return_book(self,author:str, book_name:str, user):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name) # remove from list user
        del self.rented_books[user.username][book_name] # remove from rented_books
        self.books_available[author].append(book_name)  # add to avaibale book to current author
        return f"Success returned book from user {user.username}"




