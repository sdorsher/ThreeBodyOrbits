#current version is in the notebook itself

import numpy as np
import math
def JacobiStability(npstar1x,npstar2x,npstar3x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npstar3pos=npstar3x[:,0:3]
    npstar3v=npstar3x[:,3:]
    cmcoords=(masses[0]*npstar1pos+masses[1]*npstar2pos+masses[2]*npstar3pos)/np.sum(masses)
    cmv=(masses[0]*npstar1v+masses[1]*npstar2v+masses[2]*npstar3v)/np.sum(masses)
    r3cm=npstar3pos-cmcoords
    v3cm=npstar3v-cmv
    r12=np.sqrt(np.sum((npstar1pos-npstar2pos)**2,axis=1))
    r23=np.sqrt(np.sum((npstar2pos-npstar3pos)**2,axis=1))
    r31=np.sqrt(np.sum((npstar3pos-npstar1pos)**2,axis=1))
    Omega=((masses[0]+masses[1])/r12**3)**0.5 #angular velocity of inner two stars
    Egrav=-masses[2]*(masses[0]/r31+masses[1]/r23)
    Ekinetic=masses[2]*0.5*np.sum(v3cm**2,axis=1)
    Erot=-0.5*masses[2]*Omega**2*np.sum(r3cm**2,axis=1)
    Etot=Ekinetic+Egrav+Erot
    print(Egrav,Ekinetic,Erot,Etot)
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    return deltaE, np.mean(Etot)
