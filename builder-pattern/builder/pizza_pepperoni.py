from .pizza_builder import PizzaBuilder
from .pizza import Pizza

class PizzaPepperoni(PizzaBuilder):
    """ Pizza Pepperoni Class """

    def __init__(self):
        super().__init__(Pizza())
    
    def buildSause(self):
        print("sause pepperoni")
        self._pizza.sause = "sause pepperoni"

    
    def buildDough(self):
        print("dough pepperoni")
        self._pizza.dough = "dough pepperoni"
    
    def buildFilling(self):
        print("filling pepperoni")
        self._pizza.filling = "filling pepperoni"
