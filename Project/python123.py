
import unittest
from typing import Optional, Dict, List
from datetime import datetime,date


def age_is_legal(individuals, families, tag_positions):
    warnings = []
    for indi_id in individuals:
        individual = individuals[indi_id]
        if(individual.birth != None):
            age = individual.age
            if int(age) > 150:
                if (individual.alive == True):
                    num1 = tag_positions[indi_id]['BIRT']
                    warnings.append(
                        f'ANAMOLY: INDIVIDUAL: US07, line {num1}, {individual.name} is over 150 years old and alive.')
                elif (individual.alive == False):
                    num1 = tag_positions[indi_id]['BIRT']
                    warnings.append(
                        f'ANAMOLY: INDIVIDUAL: US07, line {num1}, {individual.name} was over 150 years old when he was dead.')
    return warnings


def unique_family_by_spouse(individuals, families, tag_positions):
    warnings = []
    fams = []
    for fam_id in families:
        family = families[fam_id]
        fam = {}
        compare = False
        if family.married != None :
            fam["MARR"] = family.married
            fam["HUSB"] = family.hname
            fam["WIFE"] = family.wname
            compare = True
        if compare:
            if fam in fams:
                num = tag_positions[fam_id]['HUSB'] | tag_positions[fam_id]['WIFE'] | tag_positions[fam_id]['MARR']
                warnings.append(
                        f'ANAMOLY: FAMILY: US24, line {num}, Family contain same husband ({family.hname}), same wife ({family.wname}) and same marraige date ({family.married}) as another family.')
            else:
                fams.append(fam)
    return warnings

# class TestMethods(unittest.TestCase):
#     test class of the methods
#     def test_were_parents_over_14(self):
#         """ test were_parents_over_14 method """
#         # husband is 20 and wife is 14 at the marriage date -> Both are over 14 -> True
#         husband: Individual = Individual(_id="I0", birt={'date': "19 SEP 1995"})
#         wife: Individual = Individual(_id="I1", birt={'date': "3 JAN 2000"})
#         individuals: List[Individual] = [husband, wife]
#         family: Family = Family(husb=husband.id, wife=wife.id, marr={'date': "11 FEB 2015"})
#         self.assertTrue(were_parents_over_14(family, individuals))

#         # husband 12, wife 20 -> Only wife is over 14 -> False
#         husband: Individual = Individual(_id="I2", birt={'date': "2 MAR 2007"})
#         wife: Individual = Individual(_id="I3", birt={'date': "11 FEB 2000"})
#         individuals: List[Individual] = [husband, wife]
#         family: Family = Family(husb=husband.id, wife=wife.id, marr={'date': "11 FEB 2019"})
#         self.assertFalse(were_parents_over_14(family, individuals))

#         # husband 18, wife 12 -> Only husband is over 14 -> False
#         husband: Individual = Individual(_id="I4", birt={'date': "22 AUG 2000"})
#         wife: Individual = Individual(_id="I5", birt={'date': "5 DEC 2007"})
#         individuals: List[Individual] = [husband, wife]
#         family: Family = Family(husb=husband.id, wife=wife.id, marr={'date': "11 FEB 2018"})
#         self.assertFalse(were_parents_over_14(family, individuals))

#         # husband 13, wife 12 -> Both are under 14 -> False
#         husband: Individual = Individual(_id="I6", birt={'date': "19 SEP 2007"})
#         wife: Individual = Individual(_id="I7", birt={'date': "3 JAN 2008"})
#         individuals: List[Individual] = [husband, wife]
#         family: Family = Family(husb=husband.id, wife=wife.id, marr={'date': "11 FEB 2020"})
#         self.assertFalse(were_parents_over_14(family, individuals))

#         # husband 18, wife 16 -> Both are over 14 -> True
#         husband: Individual = Individual(_id="I8", birt={'date': "7 FEB 1980"})
#         wife: Individual = Individual(_id="I9", birt={'date': "8 FEB 1982"})
#         individuals: List[Individual] = [husband, wife]
#         family: Family = Family(husb=husband.id, wife=wife.id, marr={'date': "11 FEB 1998"})
#         self.assertTrue(were_parents_over_14(family, individuals))"""