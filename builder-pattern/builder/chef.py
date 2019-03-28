from .pizza_builder import PizzaBuilder
"""
 This is module reference to director
"""


class Chef(PizzaBuilder):
    """ Chef class """

    def __init__(self):
        self.__pizzaBuilder = None

    
    @property
    def pizzaBuilder(self):
        return self.__pizzaBuilder
    
    
    @pizzaBuilder.setter
    def pizzaBuilder(self,value):
        self.__pizzaBuilder = value
    

    def preparePizza(self):
        print(self.__pizzaBuilder)
        self.__pizzaBuilder.buildSause()
        self.__pizzaBuilder.buildDough()
        self.__pizzaBuilder.buildFilling()
