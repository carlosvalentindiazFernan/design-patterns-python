from .pizza_adapter import PizzaAdapter

class PizzaPepperoni(PizzaAdapter):
    """ Pizza Pepperoni Class """

    def doPizza(self):
        self._Pizza = 'Pepperoni'
        print("Doing Pizza Pepperoni") 

    def __str__(self):
        return 'Pizza Pepperoni Class'