"""Create a class called Integer. Upon initialization, it should receive a single parameter value (int).
 It should have 3 additional methods:
•	from_float(float_value) - creates a new instance by flooring the provided floating number.
If the value is not a float, return a message "value is not a float"
•	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
•	from_string(value) - creates a new instance by converting the string to an
integer (if the value cannot be converted, return a message "wrong type")
"""





class Integer:

    def __init__(self,value):
        self.value = value

    @staticmethod
    def __prove_if_number(value):
        if type(value)==float:
            return True
        else:
            return False

    @staticmethod
    def __number_from_roman(text):
        try:
            roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}
            i = 0
            num = 0
            while i < len(text):
                if i + 1 < len(text) and text[i:i + 2] in roman:
                    num += roman[text[i:i + 2]]
                    i += 2
                else:
                    # print(i)
                    num += roman[text[i]]
                    i += 1
            return num
        except:
            return None
    @staticmethod
    def __string_to_number(value):
        for each_digit in list(str(value)):
            if not each_digit.isdigit():
                return False
        return True






    @classmethod
    def from_float(cls,float_value):
        if Integer.__prove_if_number(float_value)==True:
            return cls(int(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls,value): # - creates a new instance by converting the roman number (as string) to an integer
        number=Integer.__number_from_roman(value)
        if type(number) !=None:
            return cls(number)

    @classmethod
    def from_string(cls,value) : #- creates a new instance by converting the string to an
#integer (if the value cannot be converted, return a message "wrong type")
        if Integer.__string_to_number(value):
            return cls(int(value))
        else:
            return "wrong type"


    def __repr__(self):
        return str(self.value)





# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_float(2.5))
# print(Integer.from_string(2.6))
#
# print("___ TEST ---")
# print(Integer.from_string(1.5))
# dr=Integer.from_float(2.5)
# print(dr.value)
#
#
# tr_num = Integer.from_roman("V")
# print(tr_num.value)
#
# print(Integer.from_string(2))
# #print(hhh.value)
#
#
#
# integer = Integer.from_string("10")
# print(type(integer.value))
