import numpy as np
import math
def getxyuvequneq(initdat,isper):
    phi,orbitangle,orbitalradius,eccentricity, masses=initdat
    print("initdat", orbitalradius, phi, eccentricity, np.cos(phi), np.sin(phi))
    metersperAU=1
    Gconstant=1
    #fix x0 y0 at one star, disregard initial data, use orbital radius as separation between stars
    #this is consistant with choice in previous part
    cosphi=np.cos(phi)
    sinphi=np.sin(phi)
    coordsep=orbitalradius #/2.
    print("coordsep",coordsep)
    #x0=orbitalradius/2.*np.cos(phi)*metersperAU
    #y0=orbitalradius/2.*np.sin(phi)*metersperAU
    count=0
    for phi0 in phi:
        if phi0==0:
            print("zero")
            #x0[count]=orbitalradius[count]/2.
            #y0[count]=0
            cosphi[count]=1.0
            sinphi[count]=0.0
        if phi0==math.pi:
            cosphi[count]=-1.0
            sinphi[count]=0.0
            print("pi")
            #x0[count]=-orbitalradius[count]/2.
            #y0[count]=0
        if phi0==math.pi/2.:
            cosphi[count]=0.0
            sinphi[count]=1.0
            #x0[count]=0
            #y0[count]=orbitalradius[count]/2.
        if phi0==3*math.pi/2.:
            cosphi[count]=0.0
            sinphi[count]=-1.0
            #x0[count]=0
            #y0[count]=-orbitalradius[count]/2.
        count+=1
    x0=coordsep*cosphi
    y0=coordsep*sinphi
    #x0[1]=0.0
    #y0[1]=0.0
    z0=np.zeros(2)
    print(x0)
    print(y0)
    v=np.zeros(2)
    a=np.zeros(2)
    ux0=np.zeros(2)
    uy0=np.zeros(2)
    uz0=np.zeros(2)
    ax0=np.zeros(2)
    ay0=np.zeros(2)
    az0=np.zeros(2)
    vx0=np.zeros(2)
    vy0=np.zeros(2)
    vz0=np.zeros(2)
    if eccentricity==1:
        #parabola
        print("parabola")
        orbitalr=orbitalradius #NO REDUCED MASS
        rperarr=np.zeros(2)
        rperarr[0]=orbitalradius*masses[1]/(masses[1]+masses[0])
        rperarr[1]=orbitalradius*masses[0]/(masses[1]+masses[0])
        coordsep=orbitalr #start at aphelion
        isper=True
        if isper:
            coordsep=orbitalr
        x0=(rperarr)*cosphi
        y0=(rperarr)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        vapsq=np.zeros(2)
        vapsq[0]=2*masses[1]**2/orbitalr/(masses[1]+masses[0])
        vapsq[1]=2*masses[0]**2/orbitalr/(masses[1]+masses[0])
        
        #vapsq=masses[1]*masses[0]/masses/orbitalr/2.
        if isper:
            vapsq[0]=2*masses[1]**2/orbitalr/(masses[1]+masses[0])
            vapsq[1]=2*masses[0]**2/orbitalr/(masses[1]+masses[0])
            #vapsq=masses[1]*masses[0]/masses/orbitalr/2.
        v=np.sqrt(vapsq)
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)
    elif eccentricity<1 and eccentricity>0:
        print("ellipse")
        #elliptical
        semimajorarr=np.zeros(2)
        semimajorarr[0]=orbitalradius*masses[1]/(masses[1]+masses[0])
        semimajorarr[1]=orbitalradius*masses[0]/(masses[1]+masses[0])
        coordsep=orbitalradius*(1+eccentricity) #start at aphelion
        orbitalrarr=semimajorarr*(1+eccentricity)
        if isper:
            orbitalrarr=semimajorarr*(1-eccentricity)
            coordsep=orbitalradius*(1-eccentricity)
        x0=(orbitalrarr)*cosphi
        y0=(orbitalrarr)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        vapsq=np.zeros(2)
        #vapsq=masses[1]*masses[0]/masses/orbitalr*(1-eccentricity)/(1+eccentricity)/4.
        vapsq[0]=masses[1]**2/(masses[0]+masses[1])*(1-eccentricity)/orbitalradius/(1+eccentricity)
        vapsq[1]=masses[0]**2/(masses[0]+masses[1])*(1-eccentricity)/orbitalradius/(1+eccentricity)
        if isper:
            #vapsq=masses[1]*masses[0]/masses/orbitalr*(1+eccentricity)/(1-eccentricity)/4.
            vapsq[0]=masses[1]**2/(masses[0]+masses[1])*(1+eccentricity)/orbitalradius/(1-eccentricity)
            vapsq[1]=masses[0]**2/(masses[0]+masses[1])*(1+eccentricity)/orbitalradius/(1-eccentricity)
        v=np.sqrt(vapsq)
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)
    elif eccentricity > 1.:
        print("hyperbola")
        #hyperbola
        semimajorarr=np.zeros(2)
        semimajorarr[0]=orbitalradius*masses[1]/(masses[1]+masses[0])
        semimajorarr[1]=orbitalradius*masses[0]/(masses[1]+masses[0])
        isper = True
        coordsep = orbitalradius*(-1+eccentricity)
        orbitalrarr=semimajorarr*(-1+eccentricity)
        if isper:
            orbitalrarr=semimajorarr*(-1+eccentricity)
            coordsep=orbitalradius*(-1+eccentricity)
        x0=(orbitalrarr)*cosphi
        y0=(orbitalrarr)*sinphi
        #orbitalr=orbitalradius #NO REDUCED MASS  (semimajor axis)
        #coordsep=orbitalr*(eccentricity-1.) #start at perihelion
        #isper=True
        #x0=(coordsep)*cosphi
        #y0=(coordsep)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        #isper:
        #vapsq=masses[1]*masses[0]/masses/orbitalr*(eccentricity+1.)/(eccentricity-1.)/4. #originally e/2.
        vapsq=np.zeros(2)
        vapsq[0]=(eccentricity+1)/orbitalradius/(eccentricity-1.)*masses[1]**2/(masses[1]+masses[0])
        vapsq[1]=(eccentricity+1)/orbitalradius/(eccentricity-1.)*masses[0]**2/(masses[1]+masses[0])
        v=np.sqrt(np.abs(vapsq))
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)

    elif eccentricity==0.0: #circular
        print("circle")
        #start at perihelion for both (eliptical, doesn't generalize to three body)
        #actually start with circular orbit
        ux0=np.zeros(2) #*149597870700
        #centrepital force balances gravitational force
        metersperAU=1 #natural units
        #G=1
        Gconstant=1
        r0=2.*orbitalradius #Mystery factor of 2
        print("r0", r0)
        v=np.zeros(2)
        #for i in np.arange(2):
        #    v[i]=np.sqrt(Gconstant*masses[(i+1)%2]/np.abs(r0[i]))
        #print(v)
        #orbital raidus is star separation for unequal mass circular orbit
        semimajor0=orbitalradius*masses[1]/(masses[1]+masses[0])
        semimajor1=orbitalradius*masses[0]/(masses[1]+masses[0])
        x0[0]=semimajor0*cosphi[0]
        x0[1]=semimajor1*cosphi[1]
        y0[0]=semimajor0*sinphi[0]
        y0[1]=semimajor1*sinphi[1]
        #vp0sq=(masses[0]+masses[1])*masses[0]/masses[1]/orbitalradius
        #vp1sq=(masses[0]+masses[1])*masses[1]/masses[0]/orbitalradius
        vp0sq=masses[1]**2/(masses[0]+masses[1])/orbitalradius
        vp1sq=masses[0]**2/(masses[0]+masses[1])/orbitalradius
        #might be m1m2/(m1+m2)/orbitalr
        v[0]=np.sqrt(vp0sq)
        v[1]=np.sqrt(vp1sq)

        ux0[0]=-v[0]*sinphi[0]
        ux0[1]=-v[1]*sinphi[1]
        uy0[0]=v[0]*cosphi[0] #initial data in y only
        uy0[1]=v[1]*cosphi[1]
        uz0=np.zeros(2)
        a=np.zeros(2)
        Fapastron=masses[1]*masses[0]/orbitalradius**2
        a=Fapastron/masses
    
        ax0=-a[0]*cosphi
        ay0=-a[1]*sinphi
        az0=np.zeros(2)
    statevec=[]
    avec=[]
    for i in np.arange(len(x0)):
        stateveci=np.array([x0[i],y0[i],z0[i],ux0[i],uy0[i],uz0[i]])
        aveci=np.array([ax0[i],ay0[i],az0[i]])
        statevec.append(stateveci)
        avec.append(aveci)
    statevecnp=np.array(statevec)
    avecnp=np.array(avec)
    return masses, statevecnp,avecnp

