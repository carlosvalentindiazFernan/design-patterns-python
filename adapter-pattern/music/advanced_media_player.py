from abc import abstractmethod,ABCMeta

class AdvancedMediaPlayer(metaclass=ABCMeta):
    """ Advanced Media Player Class """

    def playVlc(self,fileName):
        pass
    
    def playMp4(self,fileName):
        pass
        