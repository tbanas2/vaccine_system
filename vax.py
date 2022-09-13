from contextlib import nullcontext
from person import *
from time import time
import collections as c


#Want to be able to do something like add another vaccine mfg, add a new phase, and modify an existing phase for eligibility

#top level class that includes our simulation

#simulation is an OOP of a point in time - defined by what are the current authorizations we have
class simulation:
    def __init__(self, currentPhases =[], currentAuthorizations =[]):
        self.phases = currentPhases
        self.currentAuths = currentAuthorizations
        self.timeline
    def bootstrap():
        #put the authorizations into their phases
        return True

class vaxMfg:
    def __init__(self, name =''):
        self.name = name
    def __str__(self):
        return self.name
    

class vaxHistory:
    def __init__(self):
        self.intervals = ''
        self.vaxMfg =''

#Vax phase is primary series, booster 1, booster 2, etc.
class vaxPhase():
    def __init__(self,name='',authorizations=[]):
        self.name = name
        #this is basically a list of all the authorizations that comprise our current phase
        self.authorizations = authorizations
    #Add an authorization to the phase
    def addAuthorization(self,newAuth='') -> None:
        self.authorizations.append(newAuth)
    def __str__(self):
        return self.name


class timeline(c.UserList):
    def __init__(self, name = ''):
        self.name = ''
        self.data =[]
    def addPhase(self,newPhase = vaxPhase):
        self.append(newPhase)
    def returnAuthorizations(self):
        authorizations = []
        for phase in self:
            for authorization in phase:
                authorizations.append(authorization)
    authorizations = property(returnAuthorizations)

class vaxAuthorization:
    def __init__(self,name='',mfgs=[],intervals=[], volume=0, eligibleAges ='18+'):
        self.name = name
        self.mfgs =mfgs
        self.volume = 0
        self.doses = len(self.mfgs)
        self.intervals = intervals
        self.eligibileAges=eligibleAges
    def __str__(self):
            return self.name
        #can vaccines within this phases be mixed?





    



class vaxEvent:
    def __init__(self,date=1,mfg=vaxMfg, recipient = person):
        self.date = date
        self.mfg = mfg
        self.recipient = person
        person.getShot(date=self.date,mfg=self.mfg)