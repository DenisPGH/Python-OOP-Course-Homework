"""Implement the three generator functions:
•	integers() - generates an infinite amount of integers (starting from 1)
•	halves() - generates the halves of those integers (each integer / 2)
•	take(n, seq) - takes the first n halves of those integers"""
import random

"""
def solution():
    def integers():

    def halves()
        for i in integers():
            # TODO: Implement
    def take(n, seq):
        # TODO: Implement
    return (take, halves, integers)
"""
def solution():

    def integers():
        # for x in range(1,100):
        #     yield x
        amount = 1
        while True:
            a = amount
            amount += 1
            yield a


    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        result=[]
        for _ in range(n):
            result.append(next(seq))
        return result


    return (take, halves, integers)






take = solution()[0]  # [0.5, 1.0, 1.5, 2.0, 2.5]
halves = solution()[1]
print(take(5, halves()))
#print(solution()[0])

print("__TEST___")


# def integers():
#     pass
#
#
# for x in integers():
#     print(x)
# def halves():
#     for i in [1,2]:
#         yield i / 2
# for x in halves():
#     print(x)

# def integers():
#     amount = 1
#     while True:
#         a = amount
#         amount += 1
#         yield a
#
# print(integers())
# for x in integers():
#     print(x)
