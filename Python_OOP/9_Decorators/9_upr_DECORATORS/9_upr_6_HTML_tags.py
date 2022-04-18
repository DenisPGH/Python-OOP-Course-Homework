"""Create a decorator called tags. It should receive an HTML tag as a parameter,
wrap the result of a function with the given tag and return the new result.
 For more clarification, see the examples below"""
def tags(mark):
    def decorator(funk):
        def wrapper(*args):
            return f"<{mark}>{funk(*args)}</{mark}>"
        return wrapper
    return decorator




@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))


