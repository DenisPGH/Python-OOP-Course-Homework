"""The Song class should receive a name (string), a length (float), and a single (bool)
 upon initialization. It has one method:
-	get_info()
o	Returns the information of the song in this format: "{song_name} - {song_length}"

"""
class Song():
    def __init__(self,name,lenght,single):
        self.name = name
        self.lenght = lenght
        self.single = bool(single) # bool

    def get_info(self):
        return f"{self.name} - {self.lenght}"


