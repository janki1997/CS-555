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


# def list_of_upcoming_birth(individuals: List[Individual]):
#     for indi in individuals:
#         #datetime = individuals.birt
#         if individuals.deat is None:
#             if datetime != None:
#                 if individuals.birt.strftime("%Y") < datetime.today().strftime("%Y"):
#                     d =  timedelta(days=30) + datetime.today()
#                     if individuals.birt.strftime("%m %d") >=  datetime.today().strftime("%m %d"):
#                         if d.strftime("%m %d") >= individuals.birt.strftime("%m %d"):
#                             print("upcoming birthday date{individual.birt}")
#     return False

  
# def US38(individuals: List[Individual]):
#     today: datetime = datetime.now()   
#     print(today) 
#     birth = []
#     for individual in individuals:
#         if individual.deat is None:
#             if individual.birt:
#                 b_date: datetime = datetime.strptime(individual.birt['date'], "%d %b %Y")
#                 b_date = datetime(today.year, b_date.month, b_date.day)
#                 upcoming_ann = (b_date - today).days 
#                 if upcoming_ann <= 30 and upcoming_ann >= 0:
#                     birth.append([individual._id,individual.birt["date"]])
#                     print(f"✔ Family ({individual._id}): Anniversary is in upcoming days")
#                 else:
#                     print(f"✘ Family ({individual._id}): Anniversaery is not in upcoming days")
#         else:
#             print(f"✘ Family ({individual._id}): marrige didn't take place ")

#     print("List of couple who have Upcoming anniversary: ")
#     print(birth)
#     return birth
          


                

    


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



# def are_child_names_unique(family: List[Family], individuals: List[Individual]):
   

#     unique = True
#     child_first_names = []
#     for the_child_id in family.chil:
#         if the_child_id in individuals:
#             the_child = individuals[the_child_id]
#             first_name = the_child.firstAndMiddleName[0:the_child.firstAndMiddleName.find(' ')]
#             if first_name in child_first_names:
#                 unique = False
#                 print("no")
#                 # ErrorLogger.__logError__( \
#                 #     ErrorLogger._FAMILY, "US25", family.id, \
#                 #     "Child name " + first_name + " is not unique.")
#             else:
#                 child_first_names.append(first_name)
#         else:
#             print("US25 error: Child " +
#                   the_child_id +
#                   " is not in the Individuals dictionary.")

#     return unique



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
