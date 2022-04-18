"""Create a HashTable class that should have the needed functionality for a hash table, such as:
•	hash(key: str) - a function that should figure out where to store the key-value pair
•	add(key: str, value: any) - adds a new key-value pair usign the hash function
•	get(key: str) - returns the value corresponding to the given key
•	additional "magic" methods, that will make the code in the example work correctrly
"""
class HashTable_:
    __key="key"
    __value="value"
    dict_hash={}
    def __init__(self):
        self.array=[None]*4 # len is 4

    def __return_key_value_by_given_key(self,key):
        for each_pair in self.array:
            if each_pair == None:
                continue
            if self.return_hash(key)==each_pair[self.__key]:
                return each_pair[self.__value]


    # def get_hash_index(self, key: str):
    #     """return the index of wishes key"""
    #     for each_pair_index in range(len(self.array)):
    #         if key==self.array[each_pair_index][self.__key]:
    #             return f"The index of key {key} is {each_pair_index}"

    def hash(self,key:str): #"age"
        if len(self.dict_hash) >=4:
            raise Exception("Limit 4 !!!")
        if key not in self.dict_hash:
            self.dict_hash[key]=sum([ord(x) for x in list(key)])
        return self.dict_hash[key]

    def return_hash(self,key:str):
        for k,v in self.dict_hash.items():
            if k==key:
                return v
        raise ValueError(f"{key} is not in the list!!")


    def add(self,key: str, value: any):
        for each_idx in range(len(self.array)):
            if self.array[each_idx] == None:
                self.array[each_idx] ={self.__key:self.hash(key), self.__value: value}
                return
        raise Exception("Limit 4 !!!")

    def get(self,key: str):
        for each_idx in range(len(self.array)):
            if self.array[each_idx] != None:
                if self.array[each_idx][self.__key]==self.return_hash(key):
                    return self.array[each_idx][self.__value]
        raise Exception("Limit 4 !!!")

    def __getitem__(self, key):
        return self.__return_key_value_by_given_key(key)

    def __setitem__(self, key, value):
        for each_idx in range(len(self.array)):
            if self.array[each_idx]== None:
                self.array[each_idx]={self.__key:self.hash(key), self.__value:value}
                return
            raise Exception("Limit 4 !!!")




    def __len__(self):
        return len(self.array)


# table = HashTable()
#
# table["name"] = "Peter"
# table["age"] = 25
# table["Deni"] = 50
# table["Keti"] = 57
# table["Ket"] = 57
# print(table)
# print(table.get("name"))
# print(table["age"])
# #print(table["fffff"])
# print(len(table))
# """<hash_table.HashTable object at 0x00000185F4F08580>
# Peter
# 25
# 4
# """
# print("test_________")
# print(table.array)
# print(table.dict_hash)
# #print(table.get_hash_index("agef"))
import  unittest

class TestHashTable(unittest.TestCase):
    def test_start_value_of_none_return_4(self):
        hash=HashTable()
        self.assertEqual(4,len(hash.array))
        self.assertEqual([None,None,None,None],hash.array)
    def test_hash_give_string_return_asqii_value_of_sum(self):
        hash = HashTable()
        expected=sum([ord(x) for x in list("deni")])
        result=hash.hash("deni")
        self.assertEqual(expected, result)
    def test_add_return_dict(self):
        hash = HashTable()
        expected = sum([ord(x) for x in list("deni")])
        hash.add("deni",50)
        self.assertEqual([{'key' : expected, "value" : 50}, None, None, None], hash.array)
        self.assertEqual({"deni" : expected}, hash.dict_hash)

    def test_get__give__right_key__return_the_value(self):
        hash = HashTable()
        expected = sum([ord(x) for x in list("deni")])
        hash.add("deni", 50)
        result=hash.get("deni")
        self.assertEqual(50, result)
        #self.assertEqual({"deni": expected}, hash.dict_hash)

    def test_get__give__wrong_key__return_exception(self):
        hash = HashTable()
        hash.add("deni", 50)
        with self.assertRaises(Exception) as context:
            hash.get("den")
        self.assertEqual("den is not in the list!!", str(context.exception))

    def test_get__item__right_key__return_the_value(self):
        hash = HashTable()
        expected = sum([ord(x) for x in list("deni")])
        hash.add("deni", 50)
        result=hash["deni"]
        self.assertEqual(50, result)


    def test_get__item__wrong_key__return_exception(self):
        hash = HashTable()
        hash.add("deni", 50)
        with self.assertRaises(Exception) as context:
            result=hash["den"]
        self.assertEqual("den is not in the list!!", str(context.exception))

    def test_add_the_limit_is_4__raise_error(self):
        hash = HashTable()
        hash.add("deni", 50)
        hash.add("deni", 50)
        hash.add("deni", 50)
        hash.add("deni", 50)
        with self.assertRaises(Exception) as context:
            hash.add("deni", 50)
        self.assertEqual("Limit 4 !!!", str(context.exception))


    def test_setitem_the_limit_is_4__raise_error(self):
        hash = HashTable()
        hash.add("deni", 50)
        hash.add("deni", 50)
        hash.add("deni", 50)
        hash.add("deni", 50)
        with self.assertRaises(Exception) as context:
            hash["deni"]= 50
        self.assertEqual("Limit 4 !!!", str(context.exception))







if __name__=="__main__":
    unittest.main()