
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


# warnings=[]
def Unique_first_names_in_families(family: Family, individuals: List[Individual]) -> bool:
    cfirst_name=[]
    


    # birth_date: datetime = datetime.strptime(individual.birt['date'], "%d %b %Y")
    # current_date: datetime = datetime.now()
    # years_150 = timedelta(days=54750)

    # if individual.deat:
    #     death_date: datetime = datetime.strptime(individual.deat['date'], "%d %b %Y")
    #     if birth_date - death_date > timedelta(days=0):
            
    #         return False
    #     elif death_date - birth_date < years_150:
            
    #         return True

    # else:
    #     if current_date - birth_date < years_150:
            
    #         return True

  
    
    # return False

class TestApp(unittest.TestCase):
    def test_less_than_150(self):
        individual = Individual(birt={'date': "20 Mar 1985"})
        individual.deat = {'date': "15 Aug 2008"}
        self.assertTrue(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 2000"})
        self.assertTrue(less_than_150(individual))

        individual = Individual(birt={'date': "15 Feb 2012"})
        individual.deat = {'date': "21 JAN 2000"}
        self.assertFalse(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 1500"})
        self.assertFalse(less_than_150(individual))

        individual = Individual(birt={'date': "15 JAN 2006"})
        individual.deat = {'date': "15 JAN 1200"}
        self.assertFalse(less_than_150(individual))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
