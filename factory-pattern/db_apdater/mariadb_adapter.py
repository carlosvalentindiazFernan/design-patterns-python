from .dba_adapter import IBDAdapter
import mysql.connector as mariadb

class MariaDBlAdapter(IBDAdapter):
        """MariaDB Adapter Connection DBA"""
        
        __user = ""
        __host = ""
        __password = ""
        __port = ""
        __dataBase =""

        def getConnection(self):
            return mariadb.connect(
                user=self.__user, 
                password=self.__password, 
                database=self.__dataBase
            )

        def __str__(self):
            return 'MariaDB Connection Class'