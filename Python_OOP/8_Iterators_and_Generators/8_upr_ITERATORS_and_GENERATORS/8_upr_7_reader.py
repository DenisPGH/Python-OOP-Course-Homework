"""Create a generator function called read_next() which should receive a different number
 of arguments (all iterable). On each iteration, the function should return each element from each sequence."""

def read_next(*iterable):
    index = 0
    list_=list(iterable)
    list_2=[]
    [list_2.extend(x) for x in list_]
    while index <len(list_2):
        a= list_2[index]
        index += 1
        yield a

    # # nasko
    # for each in list_:
    #     for e in each:
    #         yield e








# for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
#     print(item, end='')   # string2dict

# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
#
