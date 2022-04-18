"""You are provided with a class IntegerList. It should only store integers.
 The initial integers should be set by the constructor. They are stored as a list.
  IntegerList has a functionality to add, remove_index, get, insert, get the biggest number,
   and get the index of an element. Your task is to project_ the class.
Note: You are not allowed to change the structure of the provided code"""


"""
ot @@@@@@@SOFTUNI   @@@@@@@
class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)"""
class IntegerList:
    def __init__(self,*args):
        self.integers=list(args)

    def add(self,num):
        if not isinstance(num,int):
            raise ValueError("Element is not Integer")
        self.integers.append(num)
    def remove_index(self,index):
        if index<0 or index>=len(self.integers):
            raise IndexError("Index is out of range")
        self.integers.pop(index)
    def get(self,element_index):
        if element_index < 0 or element_index >= len(self.integers):
            raise IndexError("Index is out of range")
        return self.integers[element_index]
    def insert(self,element,index):
        if index < 0 or index >= len(self.integers):
            raise IndexError("Index is out of range")
        if not isinstance(element, int):
            raise ValueError("Element is not Integer")
        self.integers.insert(index,element)
    def get_biggest(self):
        return max(self.integers)

    def get_index(self,element):
        return self.integers.index(element)



"""
Constraints
•	add operation, should add an element and returns the list.
o	If the element is not an integer, a ValueError is thrown
•	remove_index operation removes the element on that index and returns it.
o	If the index is out of range, an IndexError is thrown
•	__init__ should only take integers, and store them
•	get should return the specific element
o	If the index is out of range, an IndexError is thrown
•	insert
o	If the index is out of range, IndexError is thrown
o	If the element is not an integer, ValueError is thrown
•	get_biggest
•	get_index
Hint
Do not forget to project_ the constructor
"""
## submit only the project_
import unittest
class IntegerListTests(unittest.TestCase):
    # project_ constructor
    def test_getting_value_by_incialisation(self):
        list_=IntegerList(1)
        self.assertEqual([1], list_.integers)

    # if add correct number
    def test_adding_correct_value_return(self):
        numbers=IntegerList(1,2)
        numbers.add(2)
        self.assertEqual([1,2,2], numbers.integers)
    # project_ if not integer raise exception
    def test_if_adding_not_integer_raise_ecxception(self):
        numbers = IntegerList(1)
        with self.assertRaises(Exception) as context:
            numbers.add("d")
        self.assertEqual("Element is not Integer", str(context.exception))

    # check if remove right index
    def test_removing_right_number_by_index(self):
        numbers = IntegerList(1, 2)
        numbers.remove_index(0)
        self.assertEqual([2], numbers.integers)
    def test_if_not_corect_index_raise_error(self):
        numbers = IntegerList(1)
        with self.assertRaises(Exception) as context:
            numbers.remove_index(5)
        self.assertEqual("Index is out of range", str(context.exception))
    # project_ get element by index
    def test_get_right_number_by_index(self):
        numbers = IntegerList(1, 2)
        resutl=numbers.get(0)
        self.assertEqual(1, resutl)

    def test_if_not_corect_index_for_get_raise_error(self):
        numbers = IntegerList(1)
        with self.assertRaises(Exception) as context:
            numbers.get(5)
        self.assertEqual("Index is out of range", str(context.exception))

    # project_ insert element of index- 3 project_
    def test_giving_element_and_index_return_new_value_of_lists(self):
        numbers = IntegerList(1, 2)
        numbers.insert(3,0)
        self.assertEqual([3,1,2], numbers.integers)
    def test_giving_wrong_index__insert_function__return_error(self):
        numbers = IntegerList(1)
        with self.assertRaises(Exception) as context:
            numbers.insert(2,5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_giving_wrong_type__insert_function__return_error(self):
        numbers = IntegerList(1)
        with self.assertRaises(Exception) as context:
            numbers.insert("3",0)
        self.assertEqual("Element is not Integer", str(context.exception))

    # testing get biggest
    def test_get_biggest_return__bigest(self):
        numbers = IntegerList(1,2,6)
        result=numbers.get_biggest()
        self.assertEqual(6, result)

    # get index
    def test_get_number_by_given_index(self):
        numbers = IntegerList(1, 2, 6)
        result=numbers.get_index(2)
        self.assertEqual(1, result)



if __name__=="__main__":
    unittest.main()