

import ErrorLogger

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


def validateFamilyRoles(family: Family, individuals: List[Individual]) -> bool:
    if family.husbId not in individuals and family.wifeId not in individuals:
        return False
    if family.husbId in individuals:
        hus = individuals[family.husbId]
        if len(family.children) == len(hus.chil):
            if not childrenExistInFamily(hus.chil,family.chil):
                return False
        else:
            return False
    if family.wifeId in individuals:
        wife = individuals[family.wifeId]
        if len(family.chil) == len(wife.chil):
            if not childrenExistInFamily(wife.chil,family.chil):
                return False
        else:
            return False

    return familyMembersExist(family,individuals)


def childrenExistInFamily(parentsChildren, familyChildren):
    for parentChild in parentsChildren:
        childFound = False
        for familyChild in familyChildren:
            if familyChild == parentChild:
                childFound = True
                break
        if childFound == False:
            return False
    return True


def validSpouseExists(individId, spouseId, familyDict):

    spouseFound = False
    for i in sorted(familyDict.keys()):
        if familyDict[i].husbandId == individId:
            if spouseId == familyDict[i].wifeId:
                spouseFound = True
        if familyDict[i].wifeId == individId:
            if spouseId == familyDict[i].husbandId:
                spouseFound = True
    return spouseFound

def isIndividualInFamily(individualId, family):
    if family.husbandId == individualId:
        return True
    if family.wifeId == individualId:
        return True
    for childId in family.children:
        if childId == individualId:
            return True
    return False

def familyMembersExist(family, individualDict): 
    if family.husbandId not in individualDict:
        return False
    if family.wifeId not in individualDict:
        return False
    for childId in family.children:
        if individualDict.get(childId) is None:
            return False
    return True

def oneForOneFamilyIndividualRecords(individualDict, familyDict):
    missingIndividuals = []
    for i in sorted(individualDict.keys()):
        individ = individualDict[i]
        individExists = False
        for j in sorted(familyDict.keys()):
            if isIndividualInFamily(individ.id,familyDict[j]):
                individExists = True
        if individExists == False:
            ErrorLogger.__logError__(ErrorLogger._INDIVIDUAL,"US26",individ.id,"Individual does not exist in family")
            missingIndividuals.append(individ.id)
    missedFamilies = []
    for i in sorted(familyDict.keys()):
        fam = familyDict[i]
        if not familyMembersExist(fam,individualDict):
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US26", fam.id, "Family members don't exist in individuals")
            missedFamilies.append(fam.id)
    if len(missingIndividuals) < 1 and len(missedFamilies) < 1:
      return True
    else:
      return False


#US26 
def validateCorrespondingRecords(individualDict, familyDict):

    errors = 0
    for i in sorted(individualDict.keys()):
        individ = individualDict[i]
        if len(individ.spouse) > 0:
            #validate spouse is in family
            spouseCount = 0
            for spouseId in individ.spouse:
                if validSpouseExists(individ.id, spouseId, familyDict):
                    spouseCount = spouseCount + 1
            if spouseCount != len(individ.spouse):
                errors = errors + 1
                ErrorLogger.__logError__(ErrorLogger._INDIVIDUAL, "US26", individ.id, "Family records do not contain spouse")
        
        if len(individ.children) > 0:
            #validate children exists in fam
            childrenFoundInFamily = False
            for j in sorted(familyDict.keys()):
                if childrenExistInFamily(individ.children,familyDict[j].children):
                    childrenFoundInFamily = True
            if childrenFoundInFamily == False:
                errors = errors + 1
                ErrorLogger.__logError__(ErrorLogger._FAMILY, "US26", individ.id, "Family records do not contain children")
    return oneForOneFamilyIndividualRecords(individualDict,familyDict) and errors == 0
