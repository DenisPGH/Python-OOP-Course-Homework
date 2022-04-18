"""Create a decorator function called even_parameters. It should check if all parameters
 passed to a function are even numbers and only then execute the function and return the result.
  Otherwise, don't execute the function and return "Please use only even numbers!"""

def even_parameters(funk):
    def is_even(num):
        if type(num) != str:
            if num % 2 == 0:
                return True
            else:
                return False
    def wrapper(*args):
        if all([is_even(x) for x in args ]):
            return funk(*args)
        else:
            return "Please use only even numbers!"
    return wrapper



@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
"""
6
Please use only even numbers!
"""



@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

