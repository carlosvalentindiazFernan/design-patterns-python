from abc import abstractmethod,ABCMeta

class MediaPlayer(metaclass=ABCMeta):
    """ Media Player Class """

    @abstractmethod
    def play(self,audioType,fileName):
        pass


