from .pizza_store_adapter import PizzaStoreAdapter

class TexasStore(PizzaStoreAdapter):
    """ Texas Store Class """

    def orderPizza(pizza):
        print(f'Texas Order Pizza {pizza}')

    def __str__(self):
        return 'Texas Store Class'
