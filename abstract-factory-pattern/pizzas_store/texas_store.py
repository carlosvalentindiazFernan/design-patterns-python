from .pizza_store_adapter import PizzaStoreAdapter
from .type_store import Store
from pizza_factory.factory import PizzaFactory
from pizza_factory.type_pizza import Pizza


class TexasStore(PizzaStoreAdapter):
    """ Texas Store Class """

    def orderPizza(self,pizza):
        """ Order Pizza Pizza """ 
        
        print("Pizza Store Texas")

        if pizza.name  in [
            Pizza.CALIFORNIA.name,
            Pizza.ONIONS.name
        ]:            
            pizza = PizzaFactory().getPizza(pizza)            
            pizza.doPizza()
            pizza.prepare()
            pizza.bake()
            pizza.box()            
        else:
            raise Exception('Pizza  Invalid')

    def __str__(self):
        return 'Texas Store Class'
