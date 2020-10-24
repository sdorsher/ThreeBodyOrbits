import numpy as np
import math

def Lstability(npstar1x,npstar2x,mass0):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    npstar1L=mass0*np.cross(npstar1v,npstar1pos-npstar2pos)
    deltaL=np.abs((np.max(npstar1L[:,2])-np.min(npstar1L[:,2]))/np.mean(npstar1L[:,2]))
    return deltaL, np.mean(npstar1L)
