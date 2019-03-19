from .pizza_adapter import PizzaAdapter

class PizzaMargherita(PizzaAdapter):
    """ Pizza Margherita Class """

    def doPizza(self):
        self._Pizza = 'Margherita'
        print("Doing Pizza Margherita") 

    def __str__(self):
        return 'Pizza Margherita Class'