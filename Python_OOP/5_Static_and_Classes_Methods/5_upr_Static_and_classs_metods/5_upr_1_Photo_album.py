"""Create a class called PhotoAlbum. Upon initialization, it should receive pages (int).
 It should also have one more attribute: photos (empty matrix) representing
 the album with its pages where you should put the photos. Each page can contain only 4 photos.
 The class should also have 3 more methods:"""
import math


class PhotoAlbum:
    def __init__(self,pages):
        self.pages = pages
        self.photos=PhotoAlbum.__make_matrix(pages) # matrix 4 photos on page


    @staticmethod
    def __make_matrix(pages):
        some_matrix=[]
        for row in range(pages):
            some_matrix.append([])
        return some_matrix


    @staticmethod
    def __make_pages_from_photos_count(photos_value): #10
        result =photos_value/4

        return math.ceil(result)


    #•	from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum.
    # Note: Each page can contain 4 photos.
    @classmethod
    def from_photos_count(cls,photos_count: int):
        rows=PhotoAlbum.__make_pages_from_photos_count(photos_count)
        return cls(rows)

    #•	add_photo(label:str) - adds the photo in the first possible page and slot
    # and return "{label} photo added successfully on page {page_number(starting from 1)}
    # slot {slot_number(starting from 1)}". If there are no free slots left, return "No more free slots"
    def add_photo(self,label:str):
        for row in range(0,self.pages):
            for col in range(4):
                #print(self.photos[row][col])
                if not self.photos[row]:
                    self.photos[row].append(label)
                    #self.photos[row][col].append(label)
                    return f"{label} photo added successfully on page {row+1} slot {col+1}"
                if self.photos[row] and len(self.photos[row])<4 :
                    self.photos[row].append(label)
                    # self.photos[row][col].append(label)
                    return f"{label} photo added successfully on page {row + 1} slot {col + 1}"

        return "No more free slots"

    # •	display() - returns a string representation of each page and the photos in it.
    # Each photo is marked with "[]", and the page separation is made using 11 dashes (-).
    # For example, if we have 1 page and 2 photos:
    def display(self):
        separator="-"* 11
        result=separator+"\n"
        for row in self.photos:
            result+=' '.join(["[]" for a in row]) + "\n"
            result+=separator+"\n"
        return result.strip()



















#album = PhotoAlbum(4)
# album = PhotoAlbum.from_photos_count(10)
# print(album.add_photo("deni"))
# print(album.display())
# #print(album.photos)
# album.add_photo("d")
# album.add_photo("e")
# album.add_photo("n")
# album.add_photo("i")
# album.add_photo("P")
# album.add_photo("E")
# album.add_photo("E")
# album.add_photo("E")
# album.add_photo("E")
# album.add_photo("E")
# album.add_photo("E")
#
# #print(album.photos)
# print(album.display())




