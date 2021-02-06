
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



def lessthen_150_year_old(individuals: List[Individual]) -> bool:
    birth_date: datetime = datetime.strptime(individuals.birt['date'], "%d %b %Y")


    if individuals.deat:
        death_date: datetime = datetime.strptime(individuals.deat['date'], "%d %b %Y")
        return True if (death_date - birth_date < 150) else False
    
    else:
        return False


class TestApp(unittest.TestCase):
    def lessthen_150_year_old(self):
        individuals = Individual(birt={'date': "15 JAN 1999"}) 
        individuals.deat = {'date': "15 JAN 1994"}
        # individuals = Individual(birt={'date': "15 JAN 1000"})
        self.assertTrue(lessthen_150_year_old(individuals))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
