"""Submit only the project_ folder"""
import unittest

from test.mammal import Mammal


class TestMammal(unittest.TestCase):
    name="deni"
    type="mam"
    sound="HHHH"
    __kingdom = "animals"

    def test_constructor__kingdom__animal(self):
        deni = Mammal(self.name, self.type, self.sound)
        self.assertEqual("animals", deni._Mammal__kingdom)



    def test_constructor__if_gived_values_are_corect(self):
        deni=Mammal(self.name,self.type,self.sound)
        self.assertEqual(self.name,deni.name)
        self.assertEqual(self.type,deni.type)
        self.assertEqual(self.sound,deni.sound)

    def test_make_sound__should_return_string(self):
        deni = Mammal(self.name, self.type, self.sound)
        result=deni.make_sound()
        self.assertEqual(f"{deni.name} makes {deni.sound}",result)

    def test_get_kingdom__return_string(self):
        deni = Mammal(self.name, self.type, self.sound)
        result = deni.get_kingdom()
        self.assertEqual(self.__kingdom,result)

    def test_info_return_string(self):
        deni = Mammal(self.name, self.type, self.sound)
        result = deni.info()
        self.assertEqual(f"{deni.name} is of type {deni.type}", result)



if __name__=="__main__":
    unittest.main()



