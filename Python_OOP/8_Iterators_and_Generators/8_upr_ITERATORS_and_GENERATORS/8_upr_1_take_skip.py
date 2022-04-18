"""Create a class called take_skip. Upon initialization, it should receive a step (int) and
 a count (int). Implement the __iter__ and __next__ functions.
 The iterator should return the count numbers (starting from 0) with the given
 step. For more clarification, see the examples:"""

class take_skip:
    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.number=0
        self.counter=0
    def __iter__(self):
        return self

    def __next__(self):
        while self.counter<self.count:
            if self.counter >=1:
                self.number+=self.step
                self.counter+=1
                return self.number
            else:
                self.counter += 1
                return self.number

        raise StopIteration


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
