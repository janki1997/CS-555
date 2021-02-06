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
        
def listExwife(fam):
    l = []
    for i in fam:
        if 'WIFE' in fam[i]:
            l.append(fam[i]['WIFE'])
    return [x for n, x in enumerate(l) if x in l[:n]]



            


class TestApp(unittest.TestCase):
    """ test class of the methods """

    
    def test_listExwife(self):
        # fam3: Dict = {'F23':
        #                   {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
        #                    'CHIL': ['I19', 'I26', 'I30']},
        #               'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': 'I01'}}
        fam: Dict = {'F23':
                         {'fam': 'F23', 'MARR': 'FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                          'CHIL': ['I19', 'I26', 'I30']},
                     'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
        # self.assertEqual(us.listExHusb(fam3), ['I01'])
        self.assertEqual(listExwife(fam), [])

    # def test_List_death_family(self):
    #     hub : Individual = Individual(_id = "I1",deat={'date': "20 oct 2020"})
    #     wife : Individual = Individual(_id = "I2",deat={'date': "17 oct 2020"})
    #     chid : Individual = Individual(_id = "I3",deat={'date': "15 oct 2020"})
    #     fam : Family = Family(_id="I0", husb=hub.id,wife=wife.id,marr = {"19 oct 1998"})
    #     hub1 : Individual = Individual(_id = "I4",deat={'date': "29 oct 2019"})
    #     wife1 : Individual = Individual(_id = "I5",deat={'date': "21 oct 2020"})
    #     chid1 : Individual = Individual(_id = "I6",deat={'date': "20 SEP 2020"})
    #     fam1 : Family = Family(_id="I7", husb=hub.id,wife=wife.id)
    #     indi : List[Individual] = [hub,wife,chid,hub1,wife1,chid1]
    #     fami : List[Family] = [fam,fam1]
    #     self.assertEqual(List_death_family(indi,fami),["I0"])




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)                      