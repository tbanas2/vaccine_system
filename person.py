from vax import *

class person:
    def __init__(self,name='tom',ageGroup='18+',timeline=False):
        self.name = name
        self.ageGroup = ageGroup
        self.vaxHistory = []
        self.timeline = timeline
        self.vaxStatus = "Starting"
        self.receivedAuthorizations = []
    #input a vaccine manufacturer for this person next's shot, and add it to their record
    def getShot(self, date, mfg):
        self.vaxHistory.append((date,mfg.name))
    #This function is meant to check whether a person can 
    def vaxLog(self):
        for date,vax in self.vaxHistory:
            print(date,vax)

    def checkEligiblileAuthorizations(self):
        #Use a set to find out what phases this person is eligible for
        eligibleAuthorizations=set()
        eligiblePhases = set()
        for phase in self.timeline:
            for authorization in phase.authorizations:
                    if authorization.eligibileAges == self.ageGroup:
                        eligiblePhases.add(phase)
                        eligibleAuthorizations.add(authorization)
        return eligibleAuthorizations
                 
#This will check all the authorizations in the current timeline, and if person matches one of them, print it, intention is to try and find what 
    def checkEligiblilePhases(self):
        #Use a set to find out what phases this person is eligible for
        eligibleAuthorizations=set()
        eligiblePhases = set()
        for phase in self.timeline:
            for authorization in phase.authorizations:
                    if authorization.eligibileAges == self.ageGroup:
                        eligibleAuthorizations.add(phase)
        for phase in eligibleAuthorizations:
            eligiblePhases.add(phase)  
        return eligiblePhases
    #this will compare the person's vax log to their eligible authorizations and determine what is their current vax status

    eligibleAuthorizations = property(checkEligiblileAuthorizations)
    eligiblePhases = property(checkEligiblilePhases)

    def compareLog(self):
        #get just the mfgs out of the vax log into a list, also use this to keep track of where we are when iterating through our vax log
        receivedVaxes = []
        for d,m in self.vaxHistory:
            receivedVaxes.append(m)
        #check each eligible authorization against vax log - for first one that matches, add it to received authorizations and delete from temp vax log to move index ahead
        for authorization in self.eligibleAuthorizations:
            seriesCount = authorization.doses
            if receivedVaxes[0:seriesCount] == authorization.mfgs:
                self.receivedAuthorizations.append(authorization)
                receivedVaxes.pop(range(0,seriesCount))

