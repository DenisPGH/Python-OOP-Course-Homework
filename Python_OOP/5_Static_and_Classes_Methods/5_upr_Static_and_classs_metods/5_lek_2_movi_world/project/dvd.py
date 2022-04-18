"""Class DVD
Upon initialization, the DVD class should receive the following parameters:
 name: str, id: int, creation_year: int, creation_month: str, age_restriction: int.
 Each DVD should also have an attribute called is_rented (False by default)


Create a method called from_date(id: int, name: str, date: str, age_restriction: int) -
 it should create a new instance using the provided data.
 The date will be in the format "day.month.year" - all of them should be numbers.
Implement the __repr__ method so it returns the
 following string:
 "{id}: {name} ({creation_month} {creation_year}) has age restriction {age_restriction}. Status: {rented/not rented}"
"""

class DVD:
    def __init__(self,name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.id=id
        self.name=name
        self.is_rented=False

    @staticmethod
    def __month_from_number(number):
        """ this function return mont-str from give number of month"""
        MonthDict = {1: "January",
                     2: "February",
                     3: "March",
                     4: "April",
                     5: "May",
                     6: "June",
                     7: "July",
                     8: "August",
                     9: "September",
                     10: "October",
                     11: "November",
                     12: "December"
                     }
        return MonthDict[number]

    def __return_info_rented(self):
        if self.is_rented==True:
            return "rented"
        else:
            return "not rented"




    @classmethod
    def from_date(cls,id: int, name: str, date: str, age_restriction: int) :
        # "23.12.2020"
        info_data=date.split(".")
        cr_year=int(info_data[2])
        cr_mont=DVD.__month_from_number(int(info_data[1]))
        return cls(name,id,cr_year,cr_mont,age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {self.__return_info_rented()}"
