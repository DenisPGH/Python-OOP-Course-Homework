"""
 Each customer should also have a personal id (autoincremented, starting from 1).
 To do the incrementation, you should create a class attribute id equal to 1,
 which will keep the value of the id for the upcoming customer.
  For example, if there are no customers, the class id should be equal to 1.
   When there is one customer - the class id should be equal to 2.
Create a method called get_next_id, which returns the id that will be given to the next customer.
Implement the __repr__ method so it returns the info about the
customer in the following format: "Customer <{id}> {name}; Address: {address}; Email: {email}"
"""



class Customer:
    id=1
    new_id=0 # made this help function to safe the origin value
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        return  Customer.id
        # res=Customer.id # taka go napravi NASKO na uprj
        # Customer.id+=1
        # return res


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
