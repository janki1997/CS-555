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



def all_sister(individuals: List[Individual]) -> List:
    """ US62: boys gender should be male """

    girls = [ind for ind in individuals if ind.sex == 'F']
    sis = []

    for bs in girls:
        if bs.sex != 'F':
            print(f"✘ {bs.name}: Gender does not match!")
            sis.append(bs.name)

    return sis

# def all_sister(individuals: List[Individual]) -> List:
#     girls = [ind for ind in individuals if ind.sex == 'F']
#     sis = []

#     for boi in girls:
#         if boi.sex != 'F':
#             print(f"✘ {boi.name}: it not a sister !")
#             sis.append(boi.name)

#     return sis
    
class TestApp(unittest.TestCase):
    """ test class of the methods """
 
    
    
    def test_all_sister(self):
        """ test boys_gender_check method """
        indi1: Individual = Individual(name="Janki", sex='F')
        indi2: Individual = Individual(name="Dhruvil", sex='M')
        indi3: Individual = Individual(name="Dinky", sex='F')
        individuals: List[Individual] = [indi1, indi2, indi3]
        self.assertEqual(all_sister(individuals), [])


    # def all_sister(self):
    #     indi1: Individual = Individual(name="Janki", sex='F')
    #     indi2: Individual = Individual(name="Dhruvil", sex='M')
    #     indi3: Individual = Individual(name="Dinky", sex='F')
    #     individuals: List[Individual] = [indi1, indi2, indi3]
    #     self.assertFalse(all_sister(individuals), [])


        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)