
"""In the user.py file, create class User. Upon initialization, it should receive user_id (int)
 and username (string). The class should also have an instance attribute books that is an empty list.
  You should also create 3 instance methods:"""


class User():
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.books=[] # store all taken book from the user


    # -	info() - returns a string containing the books currently rented by the user in
    # ascending order separated by comma and space.
    def info(self):
        return ', '.join(sorted(self.books))

    #-	__str__() - override the method to get a string in the
    # following format "{user_id}, {username}, {list of rented books}"
    def __str__(self):
        return f"{self.id}, {self.username}, {self.books}"
