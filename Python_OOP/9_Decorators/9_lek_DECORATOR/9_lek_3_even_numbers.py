def even_numbers(function):
    result=[]
    def wrapper(numbers):
        for each in function(numbers):
            if each%2==0:
                result.append(each)
        return result
    return wrapper



@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))	#[2, 4]
