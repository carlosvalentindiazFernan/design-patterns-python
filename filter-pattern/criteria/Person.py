class Person:
    """ Person class """

    def __init__(self, name,gender,maritalStatus):
        self.__name = name
        self.__gender = gender
        self.__maritalStatus = maritalStatus
    
    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def maritalStatus(self):
        return self.__maritalStatus

    @name.setter 
    def name(self,value):
        self.__name = value
    
    @gender.setter
    def gender(self,value):
        self.__gender = value
    
    @maritalStatus.setter
    def maritalStatus(self, value):
        self.__maritalStatus = value