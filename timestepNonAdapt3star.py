import numpy as np
import math
import OrbitDiffEq
def timestepNonAdapt3star(numsteps,dt,xyuvaeqellipse,outputevery):
    masses,xvec0,avec0=xyuvaeqellipse
    ODEeq= OrbitDiffEq.OrbitDiffEq(masses,xvec0,avec0,0.0)
    #ODEeq.print2D()
    t=0.0
    star1x=[]
    star2x=[]
    star3x=[]
    star1a=[]
    star2a=[]
    star3a=[]
    times=[]
    rhoarr=[]
    errarr=[]
    dtarr=[]
    star1x.append(xvec0[0])
    star2x.append(xvec0[1])
    star3x.append(xvec0[2])
    star1a.append(avec0[0])
    star2a.append(avec0[1])
    star3a.append(avec0[2])
    times.append(0.0)
    rhoarr.append(1.)
    errarr.append(0.0)
    dtarr.append(dt)
    outputevery=1
    for i in np.arange(1,numsteps):
        masses,xvec,avec,t=ODEeq.timestepRK4ODE(i,dt)
        #ODEeq.print2D()
        if i%outputevery==0:
            star1x.append(xvec[0])
            star2x.append(xvec[1])
            star3x.append(xvec[2])
            star1a.append(avec[0])
            star2a.append(avec[1])
            star3a.append(avec[2])
            times.append(t)
    npstar2x=np.array(star2x)
    npstar1x=np.array(star1x)
    npstar3x=np.array(star3x)
    npstar2a=np.array(star2a)
    npstar1a=np.array(star1a)
    npstar3a=np.array(star3a)
    
    return nptimes, npstar1x, npstar2x,npstar3x, npstar1a, npstar2a,npstar3a

