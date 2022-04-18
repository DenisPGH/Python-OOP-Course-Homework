"""Create three decorators: make_bold, make_italic, make_underline,
 which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively."""


def make_bold(funk):
    def wrapper(*args):
        return f"<b>{funk(*args)}</b>"

    return wrapper


def make_italic(funk):
    def wrapper(*args):
        return f"<i>{funk(*args)}</i>"

    return wrapper


def make_underline(funk):
    def wrapper(*args):
        return f"<u>{funk(*args)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

# <b><i><u>Hello, Peter</u></i></b>

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

