import numpy as np
import math

def Lstability(npstar1x,npstar2x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npcm=(masses[0]*npstar1pos+masses[1]*npstar2pos)/np.sum(masses)
    npvcm=(masses[0]*npstar1v+masses[1]*npstar2v)/np.sum(masses)
    npstar1L=masses[0]*np.cross(npstar1v-npvcm,npstar1pos-npcm)
    npstar2L=masses[1]*np.cross(npstar2v-npvcm,npstar2pos-npcm)
    npstarLtot=npstar1L+npstar2L
    deltaL=np.abs((np.max(npstarLtot[:,2])-np.min(npstarLtot[:,2]))/np.mean(npstarLtot[:,2]))
    return deltaL, np.mean(npstarLtot),np.mean(npstarLtot), npstarLtot,npcm,npvcm
