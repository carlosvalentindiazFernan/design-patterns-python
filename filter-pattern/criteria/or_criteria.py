
class OrCriteria:
    """ Or Criteria """

    def __init__(self,criteria,oldCriteria):
        self.__criteria = criteria
        self.__oldCriteria = oldCriteria


    def meetCriteria(self,persons):
        firstCriteriaItems = self.__criteria.meetCriteria(persons)
        otherCriteriaItems = self.__oldCriteria.meetCriteria(persons)

        for person in otherCriteriaItems:
            if not firstCriteriaItems.__contains__(person):
                firstCriteriaItems.append(person)
        
        return firstCriteriaItems