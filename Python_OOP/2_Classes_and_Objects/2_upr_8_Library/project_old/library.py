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

        # -	add_user(user: User):
        # o	Adds the user if we do not have them in the library's user records already
        # o	Otherwise, returns the message "User with id = {user_id} already registered in the library!"
    def add_user(self,user):

        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.id} already registered in the library!"
    # -	remove_user(user: User):
    # o	Removes the user from the library records if present
    # o	Otherwise, returns the message "We could not find such user to remove!"
    def remove_user(self,user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    #-	change_username(user_id: int, new_username: str):
# o	If there is a record with the same user id in the library and the username is different than
    # the provided one, changes the username with the new one provided and
    # returns the message "Username successfully changed to: {new_username} for userid: {user_id}".
    # Changes his username in the rented_books dictionary as well (if present).


# o	If the new username is the same for this id, returns the following
    # message "Please check again the provided username -
    # it should be different than the username used so far!".

# o	If there is no record for the provided id returns "There is no user with id = {user_id}!"
    def change_username(self,user_id: int, new_username: str):
        for each_user in self.user_records:
            if user_id==each_user.id and each_user.username !=new_username: # same id, diff name
                if new_username in self.rented_books:
                    self.rented_books[each_user.username]=new_username
                each_user.username=new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            if user_id==each_user.id and each_user.username ==new_username: # same name, same id
                return "Please check again the provided username - it should be different than the username used so far!"
        return  f"There is no user with id = {user_id}!" # no id inside


