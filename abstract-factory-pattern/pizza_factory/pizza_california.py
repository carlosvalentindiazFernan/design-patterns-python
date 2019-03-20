from .pizza_adapter import PizzaAdapter

class PizzaCalifornia(PizzaAdapter):
    """ Pizza Californa Class """

    def __init__(self, *args, **kwargs):
        self._toppings.append("onions , chece")
    

    def doPizza(self):
        self._Pizza = 'California'
        print("Doing Pizza California") 

    def __str__(self):
        return 'Pizza California Class'