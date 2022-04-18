class Artist():
    """ this is class for return the name of artists"""
    def __init__(self,name,second_name):
        self.second_name=second_name
        self.name=name

    def full_name(self):
        return f"{self.name} {self.second_name}"



class Music():
    """ this is function, that return info for music"""
    def __init__(self,title,lyrics):
        self.title=title
        self.artist=denis
        self.lyrics=lyrics

    def print_info(self):
        return  f'This is "{self.title}" from "{self.artist}"'
    def play(self):
        return self.lyrics

denis=Artist("Denislav","Petrov")

song = Music("Title", "Lyrics")
print(song.print_info())
print(song.play())
print(song.artist.name)
