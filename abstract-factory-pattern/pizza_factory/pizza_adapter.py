from abc import abstractmethod,ABCMeta

class PizzaAdapter(metaclass=ABCMeta):
    """ Pizza Adapter abstra class """
    _Pizza = ""

    @abstractmethod
    def doPizza(self):
        """ Abstract Merthod for doing pizza """
        print("Something pizza is doing :)")


    def prepare(self):
        """ Prepare Pizza """
        print(f'Prepare Pizza {self._Pizza}')


    def bake(self):
        """ Bake pizza """
        print(f'Bake pizza {self._Pizza}')
    

    def box(self):
        """ Pizza Box """
        print(f'Box Pizza {self._Pizza}')