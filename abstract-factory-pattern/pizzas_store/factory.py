from pizza_factory.factory import PizzaFactory
from .ny_store import NYStore
from .texas_store import TexasStore
from .calif_store import CaliforniaStore
from .type_store import Store


class PizzaStoreFactory:
    """ Pizza Store Factory """

    
    def store(self,pizzaStore):
        """ Select Pizza Store """
        if pizzaStore == Store.CALIFORNIA:
            return CaliforniaStore()        
        elif pizzaStore == Store.NY:
            return NYStore()
        elif pizzaStore == Store.TEXAS:
            return TexasStore()        
        else:
            raise Exception('Pizza Store Invalid')



        """ Generate Order from  Order"""
"""

"""