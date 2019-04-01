from abc import abstractclassmethod,ABCMeta

class Criteria(metaclass=ABCMeta):
    """ Criteria Class """
    
    def meetCriteria(self,persons):
        pass
