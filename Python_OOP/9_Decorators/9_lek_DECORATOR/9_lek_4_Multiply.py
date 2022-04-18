def multiply(times):
    def decorator(function):
        def wrapper(to_add):
            result=function(to_add)
            return result*times
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3)) # 39

"""First, we add 3 to 10 = 13, and then we multiply the result by 3: 13 * 3 = 39"""

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

