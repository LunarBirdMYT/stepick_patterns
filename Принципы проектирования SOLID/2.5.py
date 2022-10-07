# Принцип разделения интерфейса. Не стоит добавлять слишком много методов в интерфейс.
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFasionedMachine(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        """Не поддерживается."""
        pass

    def scan(self, document):
        pass

# Лучше разделить интерфейсы, а потом наследовать необходимое
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scaner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scaner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scaner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionalMachine(MultiFunctionDevice):
    def __init__(self, printer, scaner) -> None:
        self.printer = printer
        self.scaner = scaner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scaner.scan(document)