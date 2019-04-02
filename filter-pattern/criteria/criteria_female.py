from .criteria import Criteria
import collections

class CriteriaFemale(Criteria):
    """ Criteria Female Class """

    def meetCriteria(self,persons):
        personsFemale  = []

        for index, person in enumerate(persons):
            if person.gender.upper() == 'FEMALE':
                personsFemale.append(person)
        
        return personsFemale


