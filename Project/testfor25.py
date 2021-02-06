# import ErrorLogger
import unittest
import datetime
from datetime import datetime, timedelta, date
from typing import Optional, Dict, List
# import user_stories as us


class Individual:
    """ holds an Individual record """
    def __init__(self, _id=None, name=None, sex=None, birt=None, alive=True, deat=False):
        """ store Individual info """
        self.id = _id
        self.name = name
        self.sex = sex
        self.birt: Optional[Dict[str, str]] = birt
        self.alive = alive
        self.deat: Optional[bool, Dict[str, str]] = deat
        self.famc: List[str] = []
        self.fams: List[str] = []

    def age(self):
        """ calculate age using the birth date """
        today = date.today()
        birthday = datetime.strptime(self.birt['date'], "%d %b %Y")
        age = today.year - birthday.year - \
              ((today.month, today.day) < (birthday.month, birthday.day))
        return age

    def info(self):
        """ return Individual info """
        alive = True if self.deat is False else False
        death = 'NA' if self.deat is False else self.deat['date']
        child = 'NA' if len(self.famc) == 0 else self.famc
        spouse = 'NA' if len(self.fams) == 0 else self.fams
        return [self.id, self.name, self.sex, self.birt['date'],
                self.age(), alive, death, child, spouse]


class Family:
    """ holds a Family record """
    def __init__(self, _id=None, marr=None, husb=None, wife=None, div=False):
        """ store Family info """
        self.id = _id
        self.marr = marr
        self.husb = husb
        self.wife = wife
        self.chil: List[str] = []
        self.div: Optional[bool, Dict[str, str]] = div

    def info(self, individuals: List[Individual]):
        """ return Family info """
        div = 'NA' if self.div is False else self.div['date']
        chil = 'NA' if len(self.chil) == 0 else self.chil
        h_name = next(individual.name for individual in individuals if individual.id == self.husb)
        w_name = next(individual.name for individual in individuals if individual.id == self.wife)

        return [self.id, self.marr['date'], div, self.husb, h_name, self.wife, w_name, chil]





def are_child_names_unique(family: List[Family], individuals: List[Individual]):
   

    unique = True
    child_first_names = []
    for the_child_id in family.chil:
        if the_child_id in individuals:
            the_child = individuals[the_child_id]
            first_name = the_child.firstAndMiddleName[0:the_child.firstAndMiddleName.find(' ')]
            if first_name in child_first_names:
                unique = False
                print("no")
                # ErrorLogger.__logError__( \
                #     ErrorLogger._FAMILY, "US25", family.id, \
                #     "Child name " + first_name + " is not unique.")
            else:
                child_first_names.append(first_name)
        else:
            print("US25 error: Child " +
                  the_child_id +
                  " is not in the Individuals dictionary.")

    return unique



class TestUS25FirstNamesUnique(unittest.TestCase):
    """
    Class TestUS25FirstNamesUnique
    Contains methods that perform unit tests to determine if the first names
    of all children in a family are unique.
    """

    def test_first_names_unique(self):
        """
        function test_first_names_unique
        builds a set of records that construct a family where all children
        have unique first names (positive test).
        """
        father_1 = Individual()
        father_1._id = "F1"
        father_1.name = "James Jonas Jamison"
        father_1.birt ="1 JAN 1910"
        

        mother_1 = Individual()
        mother_1._id = "M1"
        mother_1.name = "Janet Judy Jamison"
        mother_1.birt = "1 feb 1920"        

        # Generation 2 - Children
        child_1 = Individual()
        child_1._id = "C1"
        child_1.name = "Jacob Jarad Jamison"
        child_1.birt =" 3 feb 1955 "
        
     

        child_2 = Individual()
        child_2._id = "C2"
        child_2.name = "Jessica Joyce Jamison"
        child_2.birt ="3 feb 1957"
    

        child_3 = Individual()
        child_3._id = "C3"
        child_3.name = "Jenny Jackson Jamison"
        child_3.birt="3 feb 1960"
       

        # Family - tie them all together
        family_1 = Family()
        family_1._id = "G1F1"
        family_1.husb = father_1._id
        family_1.wife = mother_1._id
        family_1.chil.append(child_1._id)
        family_1.chil.append(child_2._id)
        family_1.chil.append(child_3._id)

        individuals_dict = {}
        individuals_dict[child_1.id] = child_1
        individuals_dict[child_2.id] = child_2
        individuals_dict[child_3.id] = child_3

        # self.assertTrue(unique_child_names.are_child_names_unique( \
        #     family_1, individuals_dict))
        self.assertTrue(are_child_names_unique(family_1,individuals_dict))

        # # Generation 1 - Parents
        # father_1: individuals = Individual(_id = "F1",name="James Jonas Jamison")
        # # father_1: individuals = Individual(_id="I20", birt={'date': "15 JAN 2020"})
        # mother_1: individuals = Individual(_id = "M1",name="Jenisha Jonas Jamison")
        # child_1: individuals = Individual(_id = "C1",name="Jamish Jonas Jamison")
        # child_2: individuals = Individual(_id = "C2",name="Jeshika Jonas Jamison")
        # child_3: individuals = Individual(_id = "C3",name="Janu Jonas Jamison")
        # individuals_dict = {child_1,child_2,child_3}
        # # individuals_dict[child_1.id] = child_1
        # # individuals_dict[child_2.id] = child_2
        # # individuals_dict[child_3.id] = child_3
        # family: Family = Family(_id="F0", husb=father_1, wife=mother_1)
        # family.chil.append(child_1)
        # family.chil.append(child_2)
        # family.chil.append(child_3)
        # # self.assertTrue(us.birth_before_death_of_parents(family, individuals))
       

        

        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
