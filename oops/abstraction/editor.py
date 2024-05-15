
from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def edit(self):
        print("edit here")

    def debug(self):
        print("debug here")

    def execute(self):
        print("execute here")

obj=Vscode()
obj.execute()