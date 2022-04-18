"""Create a class called countdown_iterator. Upon initialization, it should receive a count.
Implement the iterator to return each countdown number (from count to 0 inclusive),
 separated by a single space."""
class countdown_iterator:
    def __init__(self,count):
        self.count = count
        self.num=count

    def __iter__(self):
        return self

    def __next__(self):
        while self.num >=0:
            a=self.num
            self.num-=1
            return a
        raise StopIteration




# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")

# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")

