def printing(n,row):
    print(" " * (n - row), end="")
    for cow in range(1, row + 1):
        print('*', end=" ")
    print()


def generate_up_part(n):
    # print up part
    for row in range(1, n + 1):
        printing(n,row)

def generate_down_part(n):
    # print down part
    for row in range(n - 1, -1, -1):
        printing(n,row)


def print_romb(n):
    generate_up_part(n)
    generate_down_part(n)






