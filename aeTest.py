import numpy as np
def localMinimumIndex(values):
    mins=[]
    secondtolastval=values[0]
    lastval=values[1]
    for i in np.arange(2,len(values)):
        thisval=values[i]
        if thisval>lastval and lastval<secondtolastval:
            mins.append(i-1)
        secondtolastval=lastval
        lastval=thisval
    return mins

def findPerApHelion(npstar1x,theta0,ecc0,rad0):
    b=np.tan(theta0)
    x0,y0=npstar1x[0,0],npstar1x[0,1]
    mostb = []
    mostb1 = np.abs(1-npstar1x[:,1]/npstar1x[:,0]/b)
    mostb2=np.abs(1-b/npstar1x[:,1]*npstar1x[:,0])
    for b1,b2 in zip(mostb1,mostb2):
        mostb.append(min(b1,b2))
    indexminmostb=np.argmin(mostb[10:len(mostb)]) +10
    indexminmostb2=np.argmin(mostb[20:20+indexminmostb-20])+20 #aphelion
    assert np.abs(npstar1x[0,0]-npstar1x[indexminmostb,0])<1, "did not find aphelion"
    
    mins=localMinimumIndex(mostb[0:indexminmostb2+1]) #perhelion
    assert np.abs(mins[0]/indexminmostb2-1./2)<0.05, "did not find perihelion"
    coordper=[npstar1x[mins[0],0],npstar1x[mins[0],1]]
    coordap=[npstar1x[indexminmostb2,0], npstar1x[indexminmostb2,1]]
    print("aphelion", coordap)
    print("perihelion", coordper)
    rp=np.sqrt(np.sum(np.array(coordper)**2))
    ra=np.sqrt(np.sum(np.array(coordap)**2))
    print("r_ap", ra)
    print("r_per", rp)
    a=1/2*(rp+ra)
    print("a", a)
    e=(ra-rp)/(ra+rp)
    print("e",e)
    deltaa=np.abs(a-rad0)/rad0
    deltae=np.abs(e-ecc0)/ecc0
    print("delta a", deltaa)
    print("delta e", deltae)
    print("perhelion index", mins[0])
    print("aphelion index", indexminmostb2)
    return mins[0],indexminmostb2,coordper,coordap,rp,ra,e,a,deltae,deltaa
