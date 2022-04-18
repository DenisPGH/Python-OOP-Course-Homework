""" It can be writen more project_ for some functions, when, the list ist empty for example,
in some cases"""

import sys


class CustomList:
    def __init__(self):
        self.__my_list=[]

    # •	append(value) - Adds a value to the end of the list. Returns the list.
    def append(self,value):
        self.__my_list.append(value)
        return self.__my_list
    # •	remove(index) - Removes the value on the index. Returns the value removed.
    def remove(self,index):
        if index <0 or index >= len(self.__my_list):
            raise IndexError("CustomList Index out of range")
        return self.__my_list.pop(index)

    # •	get(index) - Returns the value on the index.
    def get(self,index):
        if index <0 or index >= len(self.__my_list):
            raise IndexError("CustomList Index out of range")
        return self.__my_list[0]
    # •	extend(iterable) - Appends the iterable to the list. Returns the new list.
    def extend(self,*args):
        self.__my_list.extend(*args)
        return self.__my_list
    # •	insert(index, value) - Adds the value on the specific index. Returns the list.
    def insert(self,index,value):
        if index <0 or index >= len(self.__my_list):
            raise IndexError("CustomList Index out of range")
        self.__my_list.insert(index,value)
        return self.__my_list
    # •	pop() - Removes the last value and returns it.
    def pop(self):
        if self.__my_list:
            return self.__my_list.pop()
        else:
            raise ValueError("Empty list!")

    #   •	clear() - Removes all values, contained in the list.
    def clear(self):
        self.__my_list=[]

    # •	index(value) - Returns the index of the given value.
    def index(self,value):
        if value not in self.__my_list:
            raise ValueError(f"CustomList has no element {value}")
        return self.__my_list.index(value)

    #•	count(value) - Returns the number of times the value is contained in the list.
    def count(self,value):
        if value not in self.__my_list:
            raise ValueError(f"CustomList has no element {value}")
        return self.__my_list.count(value)
    def reverse(self): # - Returns the values of the list in reverse order.
        return self.__my_list[::-1]

    def copy(self): # •	copy() - Returns a copy of the list.
        return self.__my_list.copy()

    def size(self): #    •	size() - Returns the length of the list.
        return len(self.__my_list)
    # •	add_first(value) - Adds the value at the beginning of the list
    def add_first(self,value):
        if len(self.__my_list)==0:
            self.__my_list.append(value)
        else:
            self.__my_list.insert(0,value)
    """•	dictionize() - Returns the list as a dictionary: 
    The keys will be each value on an even position and their values will be each value on an odd position.
     If the last value on an even position, it’s value will be " " (space)"""
    def dictionize(self):
        keys_even=[]
        values_odd=[]
        my_dict={}
        for each_ind in range(len(self.__my_list)):
            if each_ind%2==0:
                keys_even.append(self.__my_list[each_ind])
            else:
                values_odd.append(self.__my_list[each_ind])
        len_dict=max(len(values_odd),len(keys_even))
        for index in range(len_dict):
            try:
                my_dict[keys_even[index]]=values_odd[index]
            except:
                my_dict[keys_even[index]] = " "
        return my_dict

    #•	move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
    def move(self,amount): # 5 first five to end
        if amount > len(self.__my_list):
            raise IndexError("CustomList amount out of range")
        first_amount=self.__my_list[:amount]
        del self.__my_list[:amount]
        self.__my_list.extend(first_amount)
        return self.__my_list

    # - Returns the sum of the list. If the value is not a number, add the length of the value
    # to the overall number.
    def sum(self):
        result = 0
        if self.__my_list:
            for each in self.__my_list:
                if isinstance(each,str):
                    result+=len(each)
                else:
                    result+=each
            return result
        else:
            raise ValueError("List is empty!")

    #•	overbound() - Returns the index of the biggest value. If the value is not a number,
    # check it’s length
    def overbound(self):
        bigest_value=-45566666666
        index_biggest_value=0
        if self.__my_list:
            for each in range(len(self.__my_list)):
                if isinstance(self.__my_list[each],str) :
                    if bigest_value<len(self.__my_list[each]):
                        bigest_value=len(self.__my_list[each])
                        index_biggest_value=each
                    else:
                        continue

                elif bigest_value<self.__my_list[each]:
                    bigest_value=self.__my_list[each]
                    index_biggest_value=each

            return index_biggest_value
        else:
            raise ValueError("List is empty!")

    #•	underbound() - Returns the index of the smallest value. If the value is not a number,
    # check it’s length.
    def underbound(self):
        smallest_value=sys.maxsize
        index_smallest_value=0
        if self.__my_list:
            for each in range(len(self.__my_list)):
                if isinstance(self.__my_list[each],str) :
                    if smallest_value>len(self.__my_list[each]):
                        smallest_value=len(self.__my_list[each])
                        index_smallest_value=each
                    else:
                        continue

                elif smallest_value>self.__my_list[each]:
                    smallest_value=self.__my_list[each]
                    index_smallest_value=each

            return index_smallest_value
        else:
            raise ValueError("List is empty!")

"""l=CustomList()
print(l.extend(1,3,4,5))
print(l.get(0))
#l.clear()
print(l.get(0))
print(l.count(3))
l.add_first("deni")
print(l.copy())

print(l.dictionize())
print(l.move(3))
print(l.sum())
print(l.overbound())
print(l.underbound())"""

# append 1,remove 2,get 2, extend 1,insert 2,pop 1,clear 1, index 2,count 2
# reverse 1,copy 1
a=2
import unittest

class CustomlistTesta(unittest.TestCase):

    def setUp(self):
        self.cl = CustomList()
    def test_append_method_shoud_add_last_position__element(self):
        #self.cl = CustomList()
        self.cl.append(5)
        self.assertEqual([5],self.cl._CustomList__my_list)

    def test_remove__give_wrong_index__raise__error(self):
        with self.assertRaises(IndexError) as context:
            self.cl.remove(4)
        self.assertEqual("CustomList Index out of range",str(context.exception))

    def test_remove_correct_index(self):
        self.cl.append(5)
        self.cl.remove(0)
        self.assertEqual([],self.cl._CustomList__my_list)

    # next project_
    def test_get__give_wrong_index__raise__error(self):
        with self.assertRaises(IndexError) as context:
            self.cl.get(4)
        self.assertEqual("CustomList Index out of range",str(context.exception))

    def test_get_correct_index(self):
        self.cl.append(5)
        result=self.cl.get(0)
        self.assertEqual(5,result)

    def test_extend_return_new_list(self):
        self.cl.extend((1,2,3))
        self.assertEqual([1,2,3],self.cl._CustomList__my_list)

    # insert
    def test_insert__give_wrong_index__raise__error(self):
        with self.assertRaises(IndexError) as context:
            self.cl.insert(4,5)
        self.assertEqual("CustomList Index out of range", str(context.exception))

    def test_insert_correct_index(self):
        self.cl.append(5)
        result = self.cl.insert(0,5)
        self.assertEqual([5, 5], result)

    def test_pop_remove_last_index(self):
        self.cl.append(5)
        result = self.cl.pop()
        self.assertEqual([], self.cl._CustomList__my_list)
    def test_pop_empty_list__retrurn_error(self):
        with self.assertRaises(ValueError) as context:
            self.cl.pop()
        self.assertEqual("Empty list!", str(context.exception))

    def test_clear(self):
        self.cl.append(5)
        self.cl.append(5)
        self.cl.append(5)
        self.cl.clear()
        self.assertEqual([], self.cl._CustomList__my_list)
    # index
    def test_index__give_wrong_value__raise__error(self):
        value=4
        with self.assertRaises(ValueError) as context:
            self.cl.index(value)
        self.assertEqual(f"CustomList has no element {value}",str(context.exception))

    def test_index_giving_correct_value__return_the_index(self):
        self.cl.append(5)
        result=self.cl.index(5)
        self.assertEqual(0,result)

    # count project_
    def test_count__give_wrong_value__raise__error(self):
        value=4
        with self.assertRaises(ValueError) as context:
            self.cl.count(value)
        self.assertEqual(f"CustomList has no element {value}",str(context.exception))

    def test_count_giving_correct_value__return_the_index(self):
        self.cl.append(5)
        self.cl.append(5)
        self.cl.append(5)
        result=self.cl.count(5)
        self.assertEqual(3,result)
    #reverse
    def test_reverse__return__reversed_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        rsult=self.cl.reverse()
        self.assertEqual([3, 2, 1], rsult)
    def test_copy__return__copied_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        rsult = self.cl.copy()
        self.assertEqual([1, 2, 3], rsult)
        self.assertNotEqual(id(self.cl._CustomList__my_list), id(rsult))

    def test_size__return__lenght_of_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        rsult = self.cl.size()
        self.assertEqual(3, rsult)
    def test_add_first_by_empty_list(self):
        rsult = self.cl.add_first(4)
        self.assertEqual([4], self.cl._CustomList__my_list)

    def test_add_first_by_full_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.add_first(4)
        self.assertEqual([4, 1, 2, 3], self.cl._CustomList__my_list)

    def test_dictionaze_by_odd_amount_of_numbers(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        result=self.cl.dictionize()
        self.assertEqual({1 : 2, 3 : " "}, result)

    def test_dictionaze_by_even_amount_of_numbers(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        result=self.cl.dictionize()
        self.assertEqual({1 : 2, 3 : 4}, result)
    # move project_
    def test_move_amount_smaller_than_lenght_of_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        result=self.cl.move(4)
        self.assertEqual([1, 2, 3, 4], result)

    def test_move_amount_bigger_than_lenght_of_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        with self.assertRaises(IndexError) as context:
            self.cl.move(5)
        self.assertEqual("CustomList amount out of range", str(context.exception))
    #sum
    def test_sum__all_numbers__return_a_num(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        result= self.cl.sum()
        self.assertEqual(10, result)

    def test_sum___numbers_and_strings__return_a_num(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append("Deni")
        result= self.cl.sum()
        self.assertEqual(10, result)

    def test_sum___empty_list__return_a_zero(self):
        with self.assertRaises(ValueError) as context:
            self.cl.sum()
        self.assertEqual("List is empty!", str(context.exception))

    # over bound = 4 testa empty, s num, s string, s neg num
    def test_overboad__empty_list_return_exection(self):
        with self.assertRaises(Exception) as context:
            self.cl.overbound()
        self.assertEqual("List is empty!",str(context.exception))
    def test_overboad__only_nums_return_index(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        result = self.cl.overbound()
        self.assertEqual(3, result)

    def test_overboad__str_and_nums_return_index(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append("Denislav")
        result = self.cl.overbound()
        self.assertEqual(3, result)

    def test_overboad__negative_nums_return_index(self):
        self.cl.append(-1)
        self.cl.append(-2)
        self.cl.append(-3)
        self.cl.append(-0.3)
        result = self.cl.overbound()
        self.assertEqual(3, result)

    #unterbound
    def test_untebound__empty_list_return_exection(self):
        with self.assertRaises(Exception) as context:
            self.cl.underbound()
        self.assertEqual("List is empty!", str(context.exception))

    def test_untebound__only_nums_return_index(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append(4)
        result = self.cl.underbound()
        self.assertEqual(0, result)

    def test_untebound__str_and_nums_return_index(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)
        self.cl.append("Denislav")
        self.cl.append(0.1)
        result = self.cl.underbound()
        self.assertEqual(4, result)

    def test_unterbound__negative_nums_return_index(self):
        self.cl.append(-1)
        self.cl.append(-2)
        self.cl.append(-3)
        self.cl.append(-0.3)
        result = self.cl.underbound()
        self.assertEqual(2, result)


if __name__=="__main__":
    unittest.main()

















