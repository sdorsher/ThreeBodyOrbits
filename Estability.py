import numpy as np
import math
def Estability(npstar1x,npstar2x,mass0):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    nprstars12=np.sqrt(np.sum((npstar1pos-npstar2pos)**2,axis=1))
    Egrav=-mass0**2/nprstars12
    Ekinetic=mass0*0.5*(np.sum(npstar1v**2,axis=1)+np.sum(npstar2v**2,axis=1))
    Etot=Ekinetic+Egrav
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    return deltaE, np.mean(Etot)
