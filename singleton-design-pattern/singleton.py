class Singleton(type):
    """ Singleton Class """

    def __init__(cls, name, bases, *args,**kwargs):
        """ Constructor  Singleton """
        super().__init__(name, bases, *args)
        cls._instance = None

    def __call__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance =super().__call__(*args,**kwargs)
        return cls._instance
