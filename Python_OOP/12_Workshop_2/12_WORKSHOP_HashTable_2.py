"""Create a HashTable class that should have the needed functionality for a hash table, such as:
•	hash(key: str) - a function that should figure out where to store the key-value pair
•	add(key: str, value: any) - adds a new key-value pair usign the hash function
•	get(key: str) - returns the value corresponding to the given key
•	additional "magic" methods, that will make the code in the example work correctrly
"""
class HashTable:
    __start_value_capacity=4
    __none_cell=__start_value_capacity
    def __init__(self):
        self.array=[None]*self.__start_value_capacity

    def hash(self,key: str):
        hash_key=abs(hash(key))% len(self.array)
        return hash_key



    def __setitem__(self, key, value):
        #self.__none_cell=self.__start_value_capacity
        index=self.hash(key)
        if self.array[index] is None:
            self.array[index]=[]
            self.__none_cell-=1
        self.array[index].append((key,value))

        if self.__none_cell==0:
            self.__grow()

    def items(self):
        items=[]
        for each_cell in self.array:
            if each_cell is None:
                continue
            else:
                for each_pair in each_cell:
                    items.append(each_pair)
        return items

    def __grow(self):
        existing_pairs=self.items()
        self.__start_value_capacity*=2
        self.__none_cell=self.__start_value_capacity
        self.array=[None]*self.__start_value_capacity
        for k,v in existing_pairs:
            self.add(k,v)



    def add(self,key: str, value: any):
        self.__setitem__(key,value)


    def __getitem__(self, key):
        index_of_key=self.hash(key)
        for each_pair in self.array[index_of_key]:
            if each_pair[0]==key:
                return each_pair[1]

    def get(self,key: str):
        return self.__getitem__(key)



    def __len__(self):
        counter=0
        for each_cell in self.array:
            if each_cell==None:
                continue
            else:
                for each_tuple in each_cell:
                    counter+=1
        return counter


    def __repr__(self):
        result='{ '
        for each_cell in self.array:
            if each_cell==None:
                continue
            else:
                for each_pair in each_cell:
                    result+=f"{repr(each_pair[0])} : {each_pair[1]} , "

        result.strip(',')
        result+="}"
        return result

    def print_array_new_line_row(self):
        result=""
        for indx,each_row in enumerate(self.array):
            result+= f"{indx} = {each_row}\n"

        return result.strip()









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

table = HashTable()
print(table.array)
#print(table.hash("deni"))
#table["name"] = "Peter"
#table["age"] = 25

for x in range(10):
    table[f"item{x}"]=x

#print(table)
#print(table.get("name"))

#print(table["age"])
#print(len(table))
#print(table.array)

print(table.print_array_new_line_row())
print(table.hash("item3"))
print(table.get("item3"))


