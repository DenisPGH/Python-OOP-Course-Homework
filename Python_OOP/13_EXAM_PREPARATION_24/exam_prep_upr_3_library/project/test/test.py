import unittest

from project_.library import Library

class Test(unittest.TestCase):
    name="Deni"
    books_by_authors={}
    readers={}
    def test_inicialisation_danni(self):
        lib=Library(self.name)
        self.assertEqual(self.name,lib.name)
        self.assertEqual(self.books_by_authors,lib.books_by_authors)
        self.assertEqual(self.readers,lib.readers)

    def test_give_emty_name__return_error(self):
        #lib = Library("")
        with self.assertRaises(ValueError) as context:
            lib = Library("")
        self.assertEqual("Name cannot be empty string!",str(context.exception))
    def test_add_book_with_author_not_in_autors(self):
        lib = Library("Deni")
        lib.add_book("d","ddd")
        self.assertEqual({"d": ["ddd"]}, lib.books_by_authors)

    def test_add_book_with_book_not_in_autors_books(self):
        lib = Library("Deni")
        lib.add_book("d","ddd")
        lib.add_book("d","ee")
        self.assertEqual({"d": ["ddd", "ee"]}, lib.books_by_authors)
    def test_add_reader_already_in_list_return_string(self):
        lib = Library("Deni")
        lib.add_reader("deni")
        result=lib.add_reader("deni")
        self.assertEqual(f"{'deni'} is already registered in the {lib.name} library.", result)
    def test_add_reader_not_in_list_return_succes(self):
        lib = Library("Deni")
        lib.add_reader("deni")
        self.assertEqual({"deni": []}, lib.readers)

    #rent_books
    def test_rent_book__not_registred_readrer__return_error(self):
        lib = Library("Deni")
        lib.add_book("Keti","K")
        reault=lib.rent_book("deni","Keti","K")
        self.assertEqual(f"{'deni'} is not registered in the {lib.name} Library.",reault )

    def test_rent_book__not_book_authors_inlist__return_error(self):
        lib = Library("Deni")
        book_autor="Keti"
        lib.add_book("Ke","K")
        lib.add_reader("deni")
        reault=lib.rent_book("deni",book_autor,"K")
        self.assertEqual(f"{lib.name} Library does not have any {book_autor}'s books.",reault )

    def test_rent_book__not_book_titel_inlist__return_error(self):
        lib = Library("Deni")
        book_autor="Keti"
        book_tit="Krrr"
        lib.add_book("Keti","K")
        lib.add_reader("deni")
        reault=lib.rent_book("deni",book_autor,book_tit)
        self.assertEqual(f"""{lib.name} Library does not have {book_autor}'s "{book_tit}".""",reault )

    def test_rent_book__success_adding(self):
        lib = Library("Deni")
        reader_name="deni"
        book_autor = "Keti"
        book_tit = "K"
        lib.add_book("Keti", "K")
        lib.add_book("Keti", "KKK")
        lib.add_book("Keti", "Koko")
        lib.add_reader(reader_name)
        reault = lib.rent_book("deni", book_autor, book_tit)
        self.assertEqual([{book_autor: book_tit}],lib.readers[reader_name])
        self.assertEqual(["KKK", "Koko"],lib.books_by_authors[book_autor])





if __name__=="__main__":
    unittest.main()
