from pizza_factory.factory import PizzaFactory



class PizzaStoreFactory:
    """ Pizza Store Factory """

    def __init__(self, factory):
        self._factory = factory
        print(factory)

    
    def order(self,typePizza):
        """ Generate Order from  Order"""
        factory = PizzaFactory()
        pizza = factory.getPizza(typePizza)

        pizza.doPizza()
        pizza.prepare()
        pizza.bake()
        pizza.box()


        



