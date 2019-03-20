from .pizza_store_adapter import PizzaStoreAdapter
from .type_store import Store
from pizza_factory.type_pizza import Pizza
from pizza_factory.factory import PizzaFactory

class CaliforniaStore(PizzaStoreAdapter):
    """ California Store Class """

    def orderPizza(self,pizza):
        """ Order Pizza """

        print("Pizza Store California")
 
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
        return 'California Store Class'
