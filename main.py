from vax import *

import sys
sys.dont_write_bytecode = True

#bootstrapping
#Create vaccine mfgs
pfizer = vaxMfg(name='Pfizer')
johnson = vaxMfg(name = 'Johnson')
moderna = vaxMfg(name='Moderna')


#create a timeline
myTimeline = timeline(name='MyTimeline')
#Create a first phase
primaryPhase = vaxPhase(name='primary')
#add our new phase to our timeline
myTimeline.addPhase(newPhase = primaryPhase)
#add an authorization to our first phase - first pfizer series for 18+
pfizerPrimary = vaxAuthorization(name='pfizerPrimary',mfgs=[pfizer,pfizer], intervals=[0,21],volume=0.5,eligibleAges='18+')
modernaPrimary = vaxAuthorization(name='modernaPrimary',mfgs=[moderna,moderna], intervals=[0,28],volume=0.5,eligibleAges='18+')
pfizerPrimaryImmuno = vaxAuthorization(name='pfizerPrimaryImmuno',mfgs=[pfizer,pfizer,pfizer], intervals=[0,21,60],volume=0.5,eligibleAges='18+')
primaryPhase.addAuthorization(newAuth=pfizerPrimary)
primaryPhase.addAuthorization(newAuth=modernaPrimary)
primaryPhase.addAuthorization(newAuth=pfizerPrimaryImmuno)

firstBoosterPhase = vaxPhase(name='First Booster')
myTimeline.addPhase(newPhase = firstBoosterPhase)
#add a Pfizer booster for seniors
pfizerBooster = vaxAuthorization(name='Pfizer First Booster',mfgs=[pfizer],intervals=[120],volume=0.5,eligibleAges='18+')

firstBoosterPhase.addAuthorization(pfizerBooster)

tom=person(timeline=myTimeline)
tomShot=tom.getShot(date=1,mfg=pfizer)
tom.getShot(date=29,mfg=pfizer)
tom.eligiblePhases
tom.eligibleAuthorizations
tom.compareLog()
tom.receivedAuthorizations