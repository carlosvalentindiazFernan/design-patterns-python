from abc import ABCMeta
class PizzaBuilder(metaclass=ABCMeta):
    """ Pizza Builder Class"""

    def __init__(self,pizza):
        self._pizza = pizza
    
    @property
    def pizza(self):
        return self._pizza
    
    @pizza.setter
    def pizza(self,value):
        self._pizza = value

    def buildSause(self):
        pass
    
    def buildDough(self):
        pass
    
    def buildFilling(self):
        pass

