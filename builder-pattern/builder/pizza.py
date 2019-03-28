""""
 This is module reference to product  
"""

class Pizza:
    """ Pizza Class Product """

    def __init__(self):
        __sause = ""
        __dough = ""
        __filling = ""

    @property
    def sause(self):
        return self.__sause

    
    @property 
    def dough(self):
        return self.__sause
    
    
    @property
    def filling(self):
        return self.__filling
    

    @sause.setter
    def sause(self, value):
        self.__sause = value
    
    
    @dough.setter   
    def dough(self,value):
        self.__dough = value
    
    
    @filling.setter
    def filling(self,value):
        self.__filling = value