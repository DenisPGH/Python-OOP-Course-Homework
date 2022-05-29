

class User:
    def __init__(self,username:str,age:int):
        self.username = username
        self.age = age
        self.movies_liked=[]
        self.movies_owned=[]


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value=="":
            raise ValueError("Invalid username!")
        self.__username=value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age=value


    def __str__(self):
        result=""
        result+=f"Username: {self.username}, Age: {self.age}"+'\n'
        result+="Liked movies:"+'\n'
        if self.movies_liked:
            for each in self.movies_liked:
                result+=f"{each}"+'\n'
        else:
            result+=f"No movies liked."
        result+="Owned movies:"+'\n'
        if self.movies_owned:
            for each in self.movies_owned:
                result+=f"{each}"+"\n"

        else:
            result+="No movies owned."
        return result.strip()
