"""Create a single class called Account. Upon initialization, it should receive
 an owner (str) and a starting amount (int, optional, 0 by default).
 It should also have an attribute called _transactions (empty list). Create the following methods:"""
class Account:
    def __init__(self,owner,starting_amount=0):
        self.owner = owner
        self.amount = starting_amount
        self._transactions=[]

    #•	add_transaction(amount) - if the amount is not an integer,
    # raise ValueError with the message "please use int for amount".
    # Otherwise, add the amount to the transactions
    @staticmethod
    def prove_if_integer(num):
        if type(num) != int:
            return True
    def add_transaction(self,amount):
        if Account.prove_if_integer(amount):
            raise  ValueError("please use int for amount")
        self._transactions.append(amount)
        self.amount+=amount

    #•	balance() - a property that returns the sum between the amount and all the transactions
    @property
    def balance(self):
        return self.amount

    #•	validate_transaction(account: Account, amount_to_add)
#o	If the balance becomes less than zero, raise ValueError with the message
# "sorry cannot go in debt!" and break the transaction.
#o	Otherwise, complete it and return a message "New balance: {account_balance}"
    @staticmethod
    def validate_transaction(account, amount_to_add):
        #new_balnce=account.balance+amount_to_add
        if account.balance-amount_to_add<0: # trqbva da e +
            raise ValueError("sorry cannot go in debt!" )
        account.amount-=amount_to_add
        #account.add_transaction.append(amount_to_add)
        return  f"New balance: {account.amount}"


    #MAGIC
    #•	When you print an account instance, the output should be in the
    # format "Account of {owner} with starting amount: {amount}".
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    #•	When you print a representational string of an account instance,
    # the output should be in the format "Account({owner}, {amount})".
    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    #•	When you access the length of an account instance,
    # you should receive the total number of transactions made.
    def __len__(self):
        return len(self._transactions)

    # •	You should iterate over an account instance and receive each transaction as a result
    def __getitem__(self, item):
        return self._transactions[item]

    #•	You should be able to reverse the order of transactions by reversing an account instance
    def __reversed__(self):
        self._transactions=self._transactions[::-1]
        return self._transactions

    #•	You should be able to compare (>, <, >=, <=, ==, !=) two account instances by their balance amount.
    def __lt__(self, other):
        return self.balance <other.balance

    def __gt__(self, other):
        return self.balance>other.balance
        #return self.balance() >other.balance()

    def __ge__(self, other):
        return self.balance >=other.balance

    def __le__(self, other):
        return self.balance <=other.balance

    def __eq__(self, other):
        return self.balance ==other.balance

    #•	When you concatenate two accounts, you should return a new account
    # with a name - string in the format "{first_owner}&{second_owner}" and starting amount
    # - the sum between their two. Both their transactions should be added to the new account.

    @classmethod
    def new_account(cls,ow_1,ow_2,a_1 ,a_2,tr_1,tr_2):
        new_name = f"{ow_1}&{ow_2}"
        new_start_amount = a_1+a_2
        new_transaction=tr_1+tr_2
        new_object=cls(new_name,new_start_amount)
        new_object._transactions=new_transaction
        return new_object

    def __add__(self, other):
        return self.new_account(self.owner, other.owner,
                                self.amount, other.amount, self._transactions, other._transactions)













# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(f"BALANCE=  {acc.balance}") # nqma skobi nakraq
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
#
# print("____TEST____")
#
#acc2 = Account("Anna", 40)
# acc1 = Account("enn", 60)
# #print(acc2.balance())
# acc2.add_transaction(-20)
# acc2.add_transaction(20)
# acc2.add_transaction(620)
# print(acc2.balance)
# print(acc2.balance)
#print(Account.validate_transaction(acc2,10))
# a=acc1+acc2
# print(acc2._transactions)
# reversed(acc2)
# print(acc2._transactions)
#
#
