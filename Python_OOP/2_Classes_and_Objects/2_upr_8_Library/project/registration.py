

class Registration():

    def add_user(self, user,library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.id} already registered in the library!"

    # -	remove_user(user: User):
    # o	Removes the user from the library records if present
    # o	Otherwise, returns the message "We could not find such user to remove!"
    def remove_user(self, user,library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    # -	change_username(user_id: int, new_username: str):
    # o	If there is a record with the same user id in the library and the username is different than
    # the provided one, changes the username with the new one provided and
    # returns the message "Username successfully changed to: {new_username} for userid: {user_id}".
    # Changes his username in the rented_books dictionary as well (if present).

    # o	If the new username is the same for this id, returns the following
    # message "Please check again the provided username -
    # it should be different than the username used so far!".

    # o	If there is no record for the provided id returns "There is no user with id = {user_id}!"
    def change_username(self, user_id: int, new_username: str,library):
        for each_user in library.user_records:
            if user_id == each_user.id and each_user.username != new_username:  # same id, diff name
                if new_username in library.rented_books:
                    library.rented_books[each_user.username] = new_username
                each_user.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            if user_id == each_user.id and each_user.username == new_username:  # same name, same id
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"  # no id inside




