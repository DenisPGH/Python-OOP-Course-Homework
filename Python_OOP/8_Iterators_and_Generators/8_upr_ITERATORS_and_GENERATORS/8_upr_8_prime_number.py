"""Create a generator function called get_primes() which should receive a list of integer
numbers and return a list containing only the prime numbers from the initial list.
 You can learn more about prime numbers from here"""


def get_primes(list_):
    only_prime=[]
    for each in list_:
        num =each
        flag = False
        if num >1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
            if not flag:
                yield each





print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))) # [2, 3, 5]

print(list(get_primes([-2, 0, 0, 1, 1, 0]))) # []





# num = 29
# flag = False
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")