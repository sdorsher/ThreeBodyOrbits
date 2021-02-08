import numpy as np
import math
def Estability3(npstar1x,npstar2x,npstar3x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npstar3pos=npstar3x[:,0:3]
    npstar3v=npstar3x[:,3:]
    nprstars12=np.sqrt(np.sum((npstar1pos-npstar2pos)**2,axis=1))
    nprstars13=np.sqrt(np.sum((npstar1pos-npstar3pos)**2,axis=1))
    nprstars23=np.sqrt(np.sum((npstar3pos-npstar2pos)**2,axis=1))
    npcm=(masses[0]*npstar1pos+masses[1]*npstar2pos+masses[2]*npstar3pos)/np.sum(masses)
    npvcm =( masses[0]*npstar1v+masses[1]*npstar2v+masses[2]*npstar3v)/np.sum(masses)
    Egrav=-masses[0]*masses[1]/nprstars12-masses[0]*masses[2]/nprstars13-masses[1]*masses[2]/nprstars23
    Ekinetic=masses[0]*0.5*np.sum((npstar1v-npvcm)**2,axis=1)+masses[1]*0.5*np.sum((npstar2v-npvcm)**2,axis=1)+masses[2]*0.5*np.sum((npstar3v-npvcm)**2,axis=1)
    Ecmkinetic = np.sum(masses)*np.sum(npvcm**2,axis=1)
    Etot=Ekinetic+Egrav
    Eplanetgexact=-masses[0]*masses[1]/nprstars12-masses[0]*masses[2]/nprstars13
    Eplanetgapprox=-(masses[0]+masses[1])*masses[2]/np.sqrt(np.sum((npstar3pos-npcm)**2,axis=1))
    Eplanetk=masses[2]*0.5*np.sum((npstar3v-npvcm)**2,axis=1)
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    return deltaE, np.mean(Etot), Egrav, Ekinetic, Etot,Ecmkinetic,Eplanetgexact,Eplanetgapprox,Eplanetk






