from .pizza_adapter import PizzaAdapter

class PizzaChicago(PizzaAdapter):
    """ Pizza Chicago Class """

    def doPizza(self):
        self._Pizza = 'Chicago'
        print("Doing Pizza Chicago") 

    def __str__(self):
        return 'Pizza Chicago Class'