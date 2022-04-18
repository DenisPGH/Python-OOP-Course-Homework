""" Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
 Implement the iterator to return each key-value pair of the dictionary
 as a tuple of two elements (the key and the value)."""
class dictionary_iter:
    def __init__(self,kwargs):
        self.dict=kwargs
        self.lenght=len(self.dict)
        self.counter=0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.lenght:
            for k,v in self.dict.items():
                self.counter+=1
                a,b=k,v
                del self.dict[k] # not good, becaouse i del it
                return (a,b)
        raise  StopIteration



# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#
# # (1, '1')
# # (2, '2')
#
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)


