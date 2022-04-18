"""Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods,
 so the iterator returns only the vowels from the string."""
class vowels:
    alowed_vowels="aeouiyAEOUIY"
    def __init__(self,text):
        self.text = text
        self.index=0


    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index] in vowels.alowed_vowels:
                a=self.text[self.index]
                self.index += 1
                return a
            self.index+=1
        raise StopIteration






my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
