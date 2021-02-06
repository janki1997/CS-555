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



def US_38(individuals: List[Individual]):
    #warnings = []
    ub: str = ""
    for indi_id in individuals:
        individual = individuals[indi_id]
        ib: datetime = individual.birt
        print(ib)
        num = individual.name
        if individual.deat is None:
            if ib is not None:
                if ib.strftime("%Y") <= datetime.today().strftime("%Y"):
                    delta: datetime = datetime.today() + timedelta(days=30)
                    print(delta)
                    if ib.strftime("%m %d") >= datetime.today().strftime("%m %d"):
                        if delta.strftime("%m %d") >= ib.strftime("%m %d"):
                            ib.strftime('%b %d %Y')
                            if ib != ub:
                                ub = ib
                                print("upcoming{num} of {ib}")
                                # warnings.append(
                                #     f'ANOMALY: INDIVIDUAL: US38, line {num}, The upcoming birthday in next 30 days is of {individual.name} on {ib}')
                                
                                
                               
                            # names[individual.name] |= num
    print("wrong")
    return False



class TestUS25FirstNamesUnique(unittest.TestCase):
    """
    Class TestUS25FirstNamesUnique
    Contains methods that perform unit tests to determine if the first names
    of all children in a family are unique.
    """

    def US_38(self):
        """
        function test_first_names_unique
        builds a set of records that construct a family where all children
        have unique first names (positive test).
        """
        individual = Individual(_id="I1", birt={'date': "9 Nove 1997"})
        
        
        self.assertFalse(US_38(individual))
       
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
