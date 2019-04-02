
class CriteriaSingle:
    """ Criteria Single Class """

    def meetCriteria(self,persons):
        personsFemale  = []

        for index, person in enumerate(persons):
            if person.maritalStatus.upper() == 'SINGLE':
                personsFemale.append(person)
        
        return personsFemale


    