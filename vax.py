from contextlib import nullcontext
from time import time


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


class timeline(list):
    def __init__(self, name = ''):
        self.name = ''
    def addPhase(self,newPhase = vaxPhase):
        self.append(newPhase)

class vaxAuthorization:
    def __init__(self,name='',mfgs=[vaxMfg],intervals=[], volume=0, eligibleAges ='18+'):
        self.name = name
        self.mfgs =[]
        self.volume = 0
        self.doses = len(self.mfgs)
        self.intervals = intervals
        self.eligibileAges=eligibleAges
        def __str__(self):
            return self.name
        #can vaccines within this phases be mixed?

class person:
    def __init__(self,name='tom',ageGroup='18+',timeline=timeline):
        self.name = name
        self.ageGroup = ageGroup
        self.vaxHistory = []
        self.timeline = timeline
    #input a vaccine manufacturer for this person next's shot, and we'll check whether they are eligible
    def getShot(self, date, mfg):
        self.vaxHistory.append((date,mfg))
    #This function is meant to check whether a person can 
    def vaxLog(self):
        for date,vax in self.vaxHistory:
            print(date,vax)

    def check(self):
        for phase in timeline:
            for authorization in phase.authorizations:
                if authorization.eligibileAges == self.ageGroup:
                    print(authorization)



class vaxEvent:
    def __init__(self,date=1,mfg=vaxMfg, recipient = person):
        self.date = date
        self.mfg = mfg
        self.recipient = person
        person.getShot(date=self.date,mfg=self.mfg)