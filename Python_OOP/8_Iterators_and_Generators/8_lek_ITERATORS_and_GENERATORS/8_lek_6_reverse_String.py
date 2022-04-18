"""Create a generator function called reverse_text that receives a string
and yields all string characters on one line in reversed order."""
def reverse_text(text):
    for each_back in range(len(text)-1,-1,-1):
        yield text[each_back]




for char in reverse_text("step"):
    print(char, end='')
