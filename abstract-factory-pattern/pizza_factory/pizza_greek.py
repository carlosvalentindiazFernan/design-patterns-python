from .pizza_adapter import PizzaAdapter

class PizzaGreek(PizzaAdapter):
    """ Pizza Greek Class """

    def doPizza(self):
        self._Pizza = 'Greek'
        print("Doing Pizza Greek") 

    def __str__(self):
        return 'Pizza Greek Class'