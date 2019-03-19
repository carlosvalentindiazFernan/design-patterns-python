from abc import abstractmethod,ABCMeta

class PizzaAdapter(metaclass=ABCMeta):
    """ Pizza Adapter abstra class """

    @abstractmethod
    def doPizza(self):
        """ Abstract Merthod for doing pizza """
        pass

