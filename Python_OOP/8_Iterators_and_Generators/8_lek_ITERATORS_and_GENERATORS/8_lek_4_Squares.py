"""Create a generator function called squares that should receive a number n.
It should generate the squares of all numbers from 1 to n (inclusive)."""

def squares(n):
    for each in range(1,n+1):
        yield each*each




#print(list(squares(5)))