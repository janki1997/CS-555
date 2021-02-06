
import unittest
import datetime
from datetime import datetime, timedelta, date
from typing import Optional, Dict, List


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




  
def birth_before_marriage_of_parents(family: Family, individuals: List[Individual]) -> bool:
    """ user story: verify that divorce before death of either spouse """
    mrgdate = datetime.strptime(family.marr.get('date'), "%d %b %Y")
    divdate = datetime.strptime(family.div.get('date'), "%d %b %Y")
    birthdate_child = datetime.strptime(individuals.birt.get('date'), "%d %b %Y")

    if family.marr:
        if birthdate_child - mrgdate > timedelta(minutes=0) and birthdate_child - divdate < timedelta(days=275):
            print(f"({family.id}) : birth_before_marriage_of_parents")
            return True
        else:
            print(f"({family.id}) : not birth_before_marriage_of_parents")
            return False
    else:
        print(f"({family.id}) : marrige is not happen")
        return False

class TestApp(unittest.TestCase):
    def test_birth_before_marriage_of_parents(self):
        individual = Individual(_id="I20", birt={'date': "11 nov 2008"})
        family =Family(_id="I21" , marr={'date':"10 jan 2008"}, div= {'date':"15 JAN 2009"}) 
        self.assertTrue(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "11 nov 2009"})
        family =Family(_id="I21" , marr={'date':"10 may 2008"}, div= {'date':"15 jul 2008"}) 
        self.assertFalse(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "12  dec 2009"})
        family =Family(_id="I21" , marr={'date':"11 may 2008"}, div= {'date':"15 sep 2008"}) 
        self.assertFalse(birth_before_marriage_of_parents(family, individual))

        individual = Individual(_id="I20", birt={'date': "12  dec 2009"})
        family =Family(_id="I21" , marr={'date':"11 may 2009"}, div= {'date':"15 sep 2009"}) 
        self.assertTrue(birth_before_marriage_of_parents(family, individual))






       

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
