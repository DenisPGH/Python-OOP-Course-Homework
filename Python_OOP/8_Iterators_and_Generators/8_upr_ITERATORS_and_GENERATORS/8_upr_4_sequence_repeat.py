"""Create a class called sequence_repeat which should receive a sequence and
 a number upon initialization. Implement an iterator to return the given elements,
 so they form a string with a length - the given number.
 If the number is greater than the number of elements, then the sequence repeats as necessary.
 """

class sequence_repeat:
    def __init__(self,sequence,number):
        self.sequence = sequence
        self.number = number
        self.counter_index=0
        self.letter_index=0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter_index< self.number:
            for_print=self.sequence[self.letter_index]
            self.letter_index+=1
            if self.letter_index>=len(self.sequence):
                self.letter_index=0
            self.counter_index+=1
            return for_print

        raise StopIteration




# result = sequence_repeat('abc', 5) # abcab
# for item in result:
#     print(item, end ='')
#
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')



