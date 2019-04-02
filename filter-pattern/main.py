from criteria.Person import Person
from criteria.criteria_female import CriteriaFemale
from criteria.criteria_male import CriteriaMale
from criteria.criteria_single import CriteriaSingle
from criteria.and_criteria import AndCriteria
from criteria.or_criteria import OrCriteria
import collections 

def main():
    persons = []
    persons.append(Person("Robert","Male", "Single"))
    persons.append(Person("John", "Male", "Married"))
    persons.append(Person("Laura", "Female", "Married"))
    persons.append(Person("Diana", "Female", "Single"))
    persons.append(Person("Mike", "Male", "Single"))
    persons.append(Person("Bobby", "Male", "Single"))

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()

    singleMale = AndCriteria(single,male)
    singleFemale = OrCriteria(single,female)

    personsFemale = singleFemale.meetCriteria(persons)
    personsMale = singleMale.meetCriteria(persons)

    print("==== Female ====")
    for femaleP in personsFemale:
        print(femaleP.name)
    print("======= Male ======")
    for maleP in personsMale:
        print(maleP.name)


    
if __name__ == "__main__":
    main()
