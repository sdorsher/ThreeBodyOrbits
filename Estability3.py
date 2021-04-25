import numpy as np
import math
def Estability3(npstar1x,npstar2x,npstar3x,masses):
    npstar1pos=npstar1x[0:3]
    print(npstar1pos)
    npstar1v=npstar1x[3:]
    print(npstar1v)
    npstar2pos=npstar2x[0:3]
    print(npstar2pos)
    npstar2v=npstar2x[3:]
    print(npstar2v)
    npstar3pos=npstar3x[0:3]
    print(npstar3pos)
    npstar3v=npstar3x[3:]
    print(npstar3v)
    nprstars12=np.sqrt(np.sum(np.square(npstar1pos-npstar2pos)))
    print(nprstars12)
    nprstars13=np.sqrt(np.sum(np.square(npstar1pos-npstar3pos)))
    nprstars23=np.sqrt(np.sum(np.square(npstar3pos-npstar2pos)))
    npcm=(masses[0]*npstar1pos+masses[1]*npstar2pos+masses[2]*npstar3pos)/np.sum(masses)
    npvcm =( masses[0]*npstar1v+masses[1]*npstar2v+masses[2]*npstar3v)/np.sum(masses)
    Egrav=-masses[0]*masses[1]/nprstars12-masses[0]*masses[2]/nprstars13-masses[1]*masses[2]/nprstars23
    Ekinetic=masses[0]*0.5*np.sum(np.square(npstar1v))+masses[1]*0.5*np.sum(np.square(npstar2v))+masses[2]*0.5*np.sum(np.square(npstar3v))
    Ecmkinetic = 0.5*np.sum(masses)*np.sum(np.square(npvcm))
    Etot=Ekinetic+Egrav-Ecmkinetic
    Eplanetgexact=-masses[0]*masses[2]/nprstars13-masses[1]*masses[2]/nprstars23
    Eplanetgapprox=-(masses[0]+masses[1])*masses[2]/np.sqrt(np.sum(np.square(npstar3pos-npcm)))
    Eplanetk=masses[2]*0.5*np.sum(np.square(npstar3v))
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    virialE = 2*(Eplanetk)+Eplanetgapprox #should total 0 for circular motion
    return deltaE, np.mean(Etot), Egrav, Ekinetic, Etot,Ecmkinetic,Eplanetgexact,Eplanetgapprox,Eplanetk,virialE






