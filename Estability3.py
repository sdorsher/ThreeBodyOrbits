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
    Egrav=-masses[0]*masses[1]/nprstars12-masses[0]*masses[2]/nprstars12-masses[1]*masses[2]/nprstars23
    Ekinetic=masses[0]*0.5*np.sum(npstar1v**2,axis=1)+masses[1]*0.5*np.sum(npstar2v**2,axis=1)+masses[2]*0.5*np.sum(npstar3v**2,axis=1)
    Etot=Ekinetic+Egrav
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    return deltaE, np.mean(Etot), Egrav, Ekinetic, Etot
