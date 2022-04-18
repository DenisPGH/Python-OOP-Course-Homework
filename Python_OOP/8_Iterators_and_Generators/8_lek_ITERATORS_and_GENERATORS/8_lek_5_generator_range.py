"""Create a generator function called genrange that receives a start (int) and an end (int)
upon initialization.
 It should generate all the numbers from the start to the end (inclusive)."""

def genrange(start,end):
    for each in range(start,end+1):
        yield each




print(list(genrange(1, 10)))	# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]