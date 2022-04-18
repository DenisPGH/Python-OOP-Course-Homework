""" The Band class should receive a name (string) upon initialization.
 It also has an attribute albums (an empty list).
The class has three methods:
"""
from .album import Album
class Band():
    def __init__(self,name):
        self.name=name
        self.albums=[]

#-	add_album(album: Album)
# o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
# o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."
    def add_album(self,album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    #-	remove_album(album_name: str)
    # o	Removes the album from the collection and returns "Album {name} has been removed."
    # o	If the album is published, returns "Album has been published. It cannot be removed."
    # o	If the album is not in the collection, returns "Album {name} is not found."
    def remove_album(self,album_name: str):
        for each_album in self.albums:
            if album_name==each_album.username and each_album.published ==True:
                return "Album has been published. It cannot be removed."
            if album_name==each_album.username and each_album.published !=True:
                self.albums.remove(each_album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    #-	details()
    # o	Returns the information of the band, with their albums, in this format:
    # "Band {name}
    #  {album details}
    #  ...
    #  {album details}"
    def details(self):
        result=f"Band {self.name}\n"
        for each in self.albums:
            result+=f"{each.details()}\n"
        return result



