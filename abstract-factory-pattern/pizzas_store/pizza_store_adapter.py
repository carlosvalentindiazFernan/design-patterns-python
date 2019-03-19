from abc import abstractmethod,ABCMeta

class PizzaStoreAdapter(metaclass=ABCMeta):
    """ Piza Store Adapter """

    @abstractmethod
    def orderPizza(self,pizza):
        pass

    
    def __str__(self):
        return 'Pizza Store Adapter'
