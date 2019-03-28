from .pizza_builder import PizzaBuilder
from .pizza import Pizza

class PizzaOnions(PizzaBuilder):
    """ Pizza Onions Class """

    def __init__(self):
        super().__init__(Pizza())
    
    def buildSause(self):
        print("sause Onions")
        self._pizza.sause = "sause Onions"

    
    def buildDough(self):
        print("dough Onions")
        self._pizza.dough = "dough Onions"
    
    def buildFilling(self):
        print("filling Onions")
        self._pizza.filling = "filling Onions"
