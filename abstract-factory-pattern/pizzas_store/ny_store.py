from .pizza_store_adapter import PizzaStoreAdapter

class NYStore(PizzaStoreAdapter):
    """ NY Store Class """

    def orderPizza(pizza):
        print(f'NY Order Pizza {pizza}')

    def __str__(self):
        return 'NY Store Class'
