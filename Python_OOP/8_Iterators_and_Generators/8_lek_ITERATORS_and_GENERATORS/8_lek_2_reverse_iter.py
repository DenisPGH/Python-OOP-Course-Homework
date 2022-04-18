"""Create a class called reverse_iter which should receive an iterable upon initialization.
Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable
in reversed order."""

class reverse_iter:
    def __init__(self,some_list):
        self.some_list = some_list
        self.index=-1
    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index)> len(self.some_list):
            raise StopIteration
        a=self.some_list[self.index]
        self.index+=-1
        return a









# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
