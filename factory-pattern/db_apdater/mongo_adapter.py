# ### Define Mongo Connection Class
from .dba_adapter import IBDAdapter
from pymongo import MongoClient

class MongoAdapter(IBDAdapter):
    """ Mongo Adapter Connection DBA"""
    
    __user = ""
    __host = "localhost"
    __password = ""
    __port = "27017"


    def getConnection(self):
        return MongoClient(self.__host,self.__port)
    
    def __str__(self):
        return 'Mongo Connection Class'
