from .dba_adapter import IBDAdapter
import psycopg2


class PostgresAdapter(IBDAdapter):
    """ Postgres Adapter Connection Class """

    __user = ""
    __host = ""
    __password = ""
    __port = ""
    __database = ""

    def getConnection(self):
         return psycopg2.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            dbname=self.__database
        )

    def __str__(self):
        return 'Postgres Connection Class'