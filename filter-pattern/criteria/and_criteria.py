from .criteria import Criteria

class AndCriteria(Criteria):
    """ And Criteria Class """

    def __init__(self,criteria,oldCriteria):
        self.__criteria = criteria
        self.__oldCriteria = oldCriteria


    def meetCriteria(self,persons):
        firstCriteriaPersons = self.__criteria.meetCriteria(persons)
        return self.__oldCriteria.meetCriteria(firstCriteriaPersons)
    