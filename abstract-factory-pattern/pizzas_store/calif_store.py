from .pizza_store_adapter import PizzaStoreAdapter

class CaliforniaStore(PizzaStoreAdapter):
    """ California Store Class """

    def orderPizza(pizza):
        print(f'California Order Pizza {pizza}')

    def __str__(self):
        return 'California Store Class'
