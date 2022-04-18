def number_increment(numbers):
    new_values=[]
    def increase():
        for each in numbers:
            new_values.append(each+1)
        return new_values
    return increase()


#print(number_increment([1, 2, 3])) #[2, 3, 4]
