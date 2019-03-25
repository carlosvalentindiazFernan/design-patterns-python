from rectangle import Rectangle
from circle import Circle
from abc import abstractclassmethod
from collections import defaultdict

class ShareCache:
    """ Share Cache """

    __shareCache = None

    
    @abstractclassmethod
    def inizialize(self):
        self.__shareCache = defaultdict(list)

        circle =  Circle("1")
        rect = Rectangle("2")

        ShareCopy = (
            (circle.getID(),circle),
            (rect.getID(),rect)
        )

        for index , share in ShareCopy:
            self.__shareCache[index].append(share)


    @abstractclassmethod
    def getClone(self,value):
        return self.__shareCache.get(value)