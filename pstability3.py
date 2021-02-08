import numpy as np
import math

def pstability3(npstar1x,npstar2x,npstar3x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npstar3pos=npstar3x[:,0:3]
    npstar3v=npstar3x[:,3:]
    #npcm=masses[0]*npstar1pos+masses[1]*npstar2pos+masses[2]*npstar3pos
    npstar1p=masses[0]*npstar1v
    npstar2p=masses[1]*npstar2v
    npstar3p=masses[2]*npstar3v
    npstarptot=npstar1p+npstar2p+npstar3p
    pmag=np.sqrt(np.sum(npstarptot**2,axis=1))
    deltap=np.abs((np.max(pmag)-np.min(pmag))/np.mean(pmag))
    return deltap, np.mean(pmag), pmag,npstarptot
