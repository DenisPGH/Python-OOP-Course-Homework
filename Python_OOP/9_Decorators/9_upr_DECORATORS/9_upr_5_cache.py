"""Create a decorator called cache. It should store all the returned values of the recursive
function fibonacci. You are provided with this code:
You need to create a dictionary called log that will store all the n's (keys) and the
returned results (values) and attach that dictionary to the fibonacci function as a variable called log,
 so when you call it, it returns that dictionary. For more clarification, see the examples"""
import functools


def cache(func):
    dict_={}
    #@functools.wraps(func)
    def wrapper(*args):
        args=args[0]
        if args not in dict_:
            dict_[args]=func(args)
        return dict_[args]
    wrapper.log=dict_
    return wrapper




@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fibonacci(n - 1) + fibonacci(n - 2)
    #print(f"fib{n}=={result}")
    return result

fibonacci(4)
print(fibonacci.log) # {1: 1, 0: 0, 2: 1, 3: 2}

"""def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")
"""
