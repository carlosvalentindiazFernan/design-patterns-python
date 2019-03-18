from .mariadb_adapter import MariaDBlAdapter
from .mongo_adapter import MongoAdapter
from .postgres_adapter import PostgresAdapter

class DBAFactory:
    """ DBA Factory Class """

    def connection(self, dbName):
        """ Connection factory  """

        if dbName.upper() == 'MONGO':
            mong = MongoAdapter()
            print(mong)
        
        elif dbName.upper() == 'MARIADB':
            maria = MariaDBlAdapter()
            print(maria)

        elif dbName.upper() == 'POSTGRES':
            postgres = PostgresAdapter()
            print(postgres)

        else:
            raise Exception('Invalid DBA')

    def __str__(self):
        return 'DBA Factory'


