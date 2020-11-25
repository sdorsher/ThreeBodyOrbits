import numpy as np

def getelltheory(theta0,ecc0,rad0):
    ell=rad0*(ecc0**2-1.)
    return ell

def getrtheory(theta0,ecc0,rad0,t):

    ell=getelltheory(theta0,ecc0,rad0)
    r=ell/(1+ecc0*np.cos(t))
    return r

def getxtheory(theta0,ecc0,rad0,t,sgn):
    r=getrtheory(theta0,ecc0,rad0,t)
    x=sgn*(np.cos(t+theta0)*r)
    return x

def getytheory(theta0,ecc0,rad0,t,sgn):
    r=getrtheory(theta0,ecc0,rad0,t)
    y=sgn*np.sin(t+theta0)*r
    return y
