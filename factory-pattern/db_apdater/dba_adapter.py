from abc import ABCMeta, abstractmethod

### Define the abstract class


class IBDAdapter(metaclass=ABCMeta):
    """IBD ADAPTER CLASS ABSTRACTA"""
    
    @abstractmethod
    def getConnection(self):
        pass
