
"""In the user.py file, create class User. Upon initialization, it should receive user_id (int)
 and username (string). The class should also have an instance attribute books that is an empty list.
  You should also create 3 instance methods:"""


class User():
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.books=[] # store all taken book from the user

    #-	get_book(author: str, book_name: str, days_to_return: int, library: project_):
#o	If the book is available in the library adds it to the books list for this user, updates the library
# records (rented_books and available_books dicts), and returns the
# following message: "{book_name} successfully rented for the next {days_to_return} days!"
#o	If it is already rented, returns the following message "The book "{book_name}" is already
# rented and will be available in {days_to_return provided by the user rented the book} days!"
    def get_book(self,author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            if self.username not in library.rented_books:
                library.rented_books[self.username]={} # add to history for return
            library.rented_books[self.username][book_name]= days_to_return
            #library.books_available[author]=[]
            library.books_available[author].remove(book_name) # remove from avaiable for this book
            self.books.append(book_name) # add for current user
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for each_user,books in library.rented_books.items():
            for book,day_for_return in books.items():
                if book_name ==book:
                    return f'The book "{book_name}" is already rented and will be available in {day_for_return} days!'

    # -	return_book(author:str, book_name:str, library: project_):
    # o	If the book is in the user's books list, returns it in the library
    # (update books_available and rented_books class attributes) and
    # removes it from the books list for this user
    # o	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"
    def return_book(self,author:str, book_name:str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name) # remove from list user
        del library.rented_books[self.username][book_name] # remove from rented_books
        library.books_available[author].append(book_name)  # add to avaibale book to current author
        return f"Success returned book from user {self.username}"

    # -	info() - returns a string containing the books currently rented by the user in
    # ascending order separated by comma and space.
    def info(self):
        return ', '.join(sorted(self.books))

    #-	__str__() - override the method to get a string in the
    # following format "{user_id}, {username}, {list of rented books}"
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
