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

def List_recent_death_family(individuals: List[Individual],families:List[Family]):
    today: datetime = datetime.now()    
    death_list = []
     
    
    for individual in individuals:
        
        if individual.deat:
            death_date: datetime = datetime.strptime(individual.deat['date'], "%d %b %Y")
            if today - death_date < timedelta(days=30):
                death_list.append(individual.id)
                print("✔ This is the recent death within last 30 days")
                
            else:
                print("✘ This is not the recent death its not within 30 days")

    print(death_list)
  


    fam_list = []
    for family in families:
        if family.marr:
            if family.husb in death_list and family.wife in death_list or family.chil in death_list:
                fam_list.append(family.id)
    print(fam_list)
    
    return fam_list

            


class TestApp(unittest.TestCase):
    """ test class of the methods """

    def test_List_recent_death_family(self):


        hub : Individual = Individual(_id = "I1",deat={'date': "30 oct 2020"})
        wife : Individual = Individual(_id = "I2",deat={'date': "25 oct 2020"})
        chid : Individual = Individual(_id = "I3",deat={'date': "28 oct 2020"})

        fam1 : Family = Family(_id="I0", husb=hub.id,wife=wife.id,marr = {"28 oct 1998"})

        hub1 : Individual = Individual(_id = "I4",deat={'date': "22 oct 2019"})
        wife1 : Individual = Individual(_id = "I5",deat={'date': "21 oct 2020"})
        chid1 : Individual = Individual(_id = "I6",deat={'date': "7 SEP 2020"})

        fam2 : Family = Family(_id="I7", husb=hub.id,wife=wife.id)

        indi : List[Individual] = [hub,wife,chid,hub1,wife1,chid1]
        fami : List[Family] = [fam1,fam2]

        
        
        self.assertEqual(List_recent_death_family(indi,fami),["I0"])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)