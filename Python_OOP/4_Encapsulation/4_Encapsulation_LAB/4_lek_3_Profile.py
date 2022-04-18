"""Create a class called Profile. Upon initialization, it should receive:
•	username: str - the username should be between 5 and 15 characters (inclusive).
If it is not, raise a ValueError with the message "The username must be between 5 and 15 characters."
•	password: str - the password must be at least 8 characters long; it must contain at least one upper case
letter and at least one digit. If it does not, raise a ValueError with the message
"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
Hint: Use Getters and Setters to name-mangle them.
Override the __str__() method of the base class, so it returns: "You have a profile with username:
 "{username}" and password: {"*" with the length of password}".
"""
class Profile:
    __min_lenght_username=5
    __max_lenght_username=15
    __error_passowrd="The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __name_validator(self,name):
        if not self.__min_lenght_username <= len(name) <self.__max_lenght_username:
            raise ValueError(f"The username must be between {self.__min_lenght_username} and {self.__max_lenght_username} characters.")

    def __passwrord_validator(self, password):
        if len(password)<8: # must 8 char long
            raise ValueError(self.__error_passowrd)
        if not any([x for x in list(password) if x.isdigit()]): # must one digite
            raise ValueError(self.__error_passowrd)
        if not any([x for x in list(password) if x.isupper()]): # must one uppercase
            raise ValueError(self.__error_passowrd)




    @property
    def username(self):
        return self.__name
    @username.setter
    def username(self, value):
        self.__name_validator(value)
        self.__name=value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__passwrord_validator(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: ' \
               f'"{self.username}" and password: {"*"*len(self.password) }'


#profile_with_invalid_password = Profile('My_username', 'My-password')


#profile_with_invalid_username = Profile('Too_long_username', 'Any')

#correct_profile = Profile("Username", "Passw0rd")
#print(correct_profile)

#d=Profile("Denis","Denislav1")
