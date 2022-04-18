from abc import  ABC,abstractmethod

class AbstractFactroy(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError


class Chair:
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return self._name


class Sofa:
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return self._name

class Table:
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactroy):
    def create_chair(self):
        return Chair("victorian chair")

    def create_sofa(self):
        return Sofa("victorian Sofa")

    def create_table(self):
        return  Table("victorian table")


class ModernFactory(AbstractFactroy):
    def create_chair(self):
        return Chair("modern chair")

    def create_sofa(self):
        return Sofa("modern  Sofa")

    def create_table(self):
        return Table("modern  table")


class FutoristicFactory(AbstractFactroy):
    def create_chair(self):
        return Chair("Futoristic chair")

    def create_sofa(self):
        return Sofa("Futoristic  Sofa")

    def create_table(self):
        return Table("Futoristic table")












