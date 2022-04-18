"""Import the time module. Create a decorator called exec_time. It should calculate
how much time a function needs to be executed. See the examples for more clarification."""
import functools
import time

def exec_time(funk):
    @functools.wraps(funk)
    def wrapper(*args):
        start=time.time()
        result=funk(*args)
        end=time.time()
        return f"Proccess '{funk.__name__}' done for {end-start:.4f} seconds"
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000)) # 0.8342537879943848

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)])) #0.14537858963012695


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop()) #0.4199554920196533





