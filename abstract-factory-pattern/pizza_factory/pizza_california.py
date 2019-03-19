from .pizza_adapter import PizzaAdapter

class PizzaCalifornia(PizzaAdapter):
    """ Pizza Californa Class """

    def doPizza(self):
        print("Doing Pizza California") 

    def __str__(self):
        return 'Pizza California Class'