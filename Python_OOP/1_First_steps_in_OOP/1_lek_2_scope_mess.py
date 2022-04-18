x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal  x # change here
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x # change here
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
""" output now 
global
outer: local
inner: nonlocal
outer: local
global
"""
""" expected output"""
# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!
