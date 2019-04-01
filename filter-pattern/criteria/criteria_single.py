
class CriteriaSingle:
    """ Criteria Single Class """

    def meetCriteria(self,persons):
        personsFemale  = []

        for index, person in enumerate(persons):
            if person.maritalStatus == 'SINGLE':
                personsFemale[index] = person
        
        return personsFemale


    