import re
pattern= r"(?P<name>([A-Za-z0-9]+))\@(?P<mail>([a-z]+))\.(?P<domain>([a-z]+))"


mails = ["gmail", "softuni"]
domains = ["com", "bg"]


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails # with set() is much better!!!!!
        self.domains = domains




    def __is_name_valid(self,name): # - returns whether the name is greater than or equal to the min_length (True/False)
        if len(name)<self.min_length:
            return False
        return True
    def __is_mail_valid(self,mail): # - returns whether the mail is in the possible mails list (True/False)
        if mail not in self.mails:
            return False
        return True

    def __is_domain_valid(self,domain): # - returns whether the domain is in the possible domains list (True/False)
        if domain not in self.domains:
            return False
        return True
    def validate(self,email): #  "pe77er@gmail.com"
        result=re.finditer(pattern,email)
        name = ""
        mail = ""
        domain = ""
        for each in result:
            name=each.group("name")
            mail=each.group("mail")
            domain=each.group("domain")

        if  self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        else:
            return False





"""Create three methods that should not be accessed outside the class:
•	is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
•	is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
•	is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)
Create one public method:
•	validate(email) - using the three methods returns whether the email is valid (True/False)
"""









# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
