"""You are provided with code containing class IEmail and class Email.
 The code does not follow the principle of single responsibility (the Email class has 2 responsibilities).
  Create a new class - IContent, and a class that inherits it called MyContent to split the responsibilities."""

from abc import ABC, abstractmethod
class IContent(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def format(self):
        pass


class MyContent(IContent):
    def __init__(self,content):
        super().__init__()
        self.content=content

    def format(self):
        #return ''.join(['<MyML>', self.content, '</MyML>'])
        return ''.join(['<DENI>', self.content, '</DENI>'])



class IEmail(ABC):


    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


    @abstractmethod
    def set_content(self, receiver):
        pass



class Email(IEmail):

    def __init__(self, protocol):
        super().__init__()
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        if content.content !=None:
            self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

print("After")
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
"""BEFORE
Sender: I'm qmal
Receiver: I'm james
Content:
<myML>
Hello, there!
</myML>

AFTER:
Sender: I'm qmal
Receiver: I'm james
Content:
<MyML>Hello, there!</MyML>

"""
