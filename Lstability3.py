import numpy as np
import math

def Lstability3(npstar1x,npstar2x,npstar3x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npstar3pos=npstar3x[:,0:3]
    npstar3v=npstar3x[:,3:]
    npcm=(masses[0]*npstar1pos+masses[1]*npstar2pos+masses[2]*npstar3pos)/np.sum(masses)
    npvcm=(masses[0]*npstar1v+masses[1]*npstar2v+masses[2]*npstar3v)/np.sum(masses)
    npstar1L=masses[0]*np.cross((npstar1v-npvcm),npstar1pos-npcm)
    npstar2L=masses[1]*np.cross((npstar2v-npvcm),npstar2pos-npcm)
    npstar3L=masses[2]*np.cross((npstar3v-npvcm),npstar3pos-npcm)
    npstarLtot=npstar1L+npstar2L+npstar3L
    deltaL=np.abs((np.max(npstarLtot[:,2])-np.min(npstarLtot[:,2]))/np.mean(npstarLtot[:,2]))
    return deltaL, np.mean(npstarLtot), npstarLtot,npcm,npvcm
