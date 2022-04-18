"""Create a generator function called possible_permutations() which should receive a list and
return lists with all possible permutations between its elements."""

# def possible_permutations(list_): #[1, 2, 3] [1,4,5,6]
#     lenght_end_list=len(list_)
#     start_index=0
#     current_row=0
#     end_rows=(lenght_end_list-1)*lenght_end_list
#
#     while current_row<end_rows:
#         new_list = []
#         for first in range(start_index,lenght_end_list):
#             new_list.append(list_[first])
#             while len(new_list)<=lenght_end_list:
#                 new_list.extend(list_[1:])
#         current_row+=1
#         yield new_list

def possible_permutations(elements):

    if len(elements) <=1:
        yield elements
    else:
        counter = 0
        for perm in possible_permutations(elements[1:]):
            for i in range(len(elements)):
                #yield perm[:i] + elements[0:1] + perm[i:]
                yield perm[:i] + elements[0:1] + perm[i:]
            counter+=1












[print(n) for n in possible_permutations([1, 2, 3])]
# print("TST=========")
# print("TST=========")
#[print(n) for n in possible_permutations([5, 6, 7, 8])]


"""
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""