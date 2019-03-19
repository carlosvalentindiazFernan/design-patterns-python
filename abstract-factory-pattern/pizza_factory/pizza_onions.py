from .pizza_adapter import PizzaAdapter

class PizzaOnions(PizzaAdapter):
    """ Pizza Onions Class """

    def doPizza(self):
        print("Doing Pizza Onions") 

    def __str__(self):
        return 'Pizza Onions Class'