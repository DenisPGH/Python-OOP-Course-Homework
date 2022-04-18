"""Create a decorator called logged. It should return the name of the function that is
being called and its parameters. It should also return the result of the execution of the
 function being called. See the examples for more clarification."""
from functools import wraps


def logged(funk):
    def wrapper(*args):
        result=funk(*args)
        count=len(args)
        return (f"you called {funk.__name__}{args}\nit returned {result}")

    return wrapper


"""
you called func(4, 4, 4)
it returned 6
"""
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
