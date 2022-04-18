import functools


def vowel_filter(function):
    vowel="aeoieyAEOIEY"
    new_list=[]
    #@functools.wraps(function)
    def wrapper():
        result=function()
        for each in result:
            if each in vowel:
                new_list.append(each)
        return new_list
    return wrapper



@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]



print(get_letters()) # ["a", "e"]
