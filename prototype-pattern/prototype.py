import copy

class ProtoType:
    """ ProtoType Class """

    _type = None
    _id = None

    def getTye(self):
        return self._type

    def getID(self):
        return self._id
    
    def clone(self):
        return copy.copy(self)


    