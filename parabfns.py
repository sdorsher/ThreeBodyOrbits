import numpy as np

def getrtheory(theta0, ecc0, rad0, t):
    return 2*rad0*1./(1+np.cos(t))

def getxtheory(theta0,ecc0,rad0,t,sgn):
    r=getrtheory(theta0,ecc0,rad0,t)
    x=sgn*r*np.cos(t-theta0)
    return x

def getytheory(theta0,ecc0,rad0,t,sgn):
    r=getrtheory(theta0,ecc0,rad0,t)
    y=sgn*r*np.sin(t-theta0)
    return y
    
