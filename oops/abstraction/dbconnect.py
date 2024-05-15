
from abc import ABC,abstractmethod

class Dbconnect(ABC):

    @abstractmethod
    def __init__(self, user, password, port, database ):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass

class Mydb(Dbconnect):

    def __init__(self, user, password, port, database):
       self.user=user
       self.password=password
       self.port=port
       self.database=database

    def connect(self):
        print("database connected")

    def execute_query(self):
        print("execution done")

    def close(self): 
        print("close connection")

obj=Mydb("asha", "asha@123", "port1", "mysql" )
obj.connect()