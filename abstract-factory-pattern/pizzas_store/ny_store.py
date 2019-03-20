from .pizza_store_adapter import PizzaStoreAdapter
from .type_store import Store
from pizza_factory.factory import PizzaFactory
from pizza_factory.type_pizza import Pizza

class NYStore(PizzaStoreAdapter):
    """ NY Store Class """
    
    def orderPizza(self,pizza):
        """ Order Pizza Pizza """         
        print("Pizza Store NY")

        if pizza.name  in [
            Pizza.CALIFORNIA.name,
            Pizza.ONIONS.name,
            Pizza.PEPPERONI.name
        ]:            
            pizza = PizzaFactory().getPizza(pizza)            
            pizza.doPizza()
            pizza.prepare()
            pizza.bake()
            pizza.box()            
            
        else:
            raise Exception('Pizza Pizza Invalid')

    def __str__(self):
        return 'NY Store Class'
