from .criteria import Criteria
import collections

class CriteriaMale(Criteria):
    """ Criteria Male Class """

    def meetCriteria(self,persons):
        personMale  = []

        for index, person in enumerate(persons):
            if person.gender.upper() == 'MALE':
                personMale.append(person)
        
        return personMale


