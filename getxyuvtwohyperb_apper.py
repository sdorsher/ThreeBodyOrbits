import numpy as np
import math
def getxyuveqtwohyperbolas(initdat,isper):
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
    ux0=0.
    uy0=0.
    uz0=0.
    ax0=0.
    ay0=0.
    az0=0.
    vx0=0.
    vy0=0.
    vz0=0.
    if eccentricity==1:
        #elliptical
        orbitalr=orbitalradius #NO REDUCED MASS
        coordsep=2*orbitalr #start at aphelion
        isper=True
        if isper:
            coordsep=orbitalr
        x0=(coordsep)*cosphi
        y0=(coordsep)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        #v= np.sqrt(masses[1]*masses[0]/masses*(2./starsep-1./(2*orbitalr)))
        vapsq=masses[1]*masses[0]/masses/orbitalr/2.
        if isper:
            vapsq=masses[1]*masses[0]/masses/orbitalr/2.
        #vapsq=masses[1]*masses[0]/masses*(1./(coordsep)-1./orbitalr)/2.
        v=np.sqrt(vapsq)
        #v= np.sqrt(masses[1]*masses[0]/masses*(1./orbitalr-2./starsep))
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)
    elif eccentricity<1 and eccentricity>0:
        #elliptical
        orbitalr=orbitalradius #NO REDUCED MASS
        coordsep=orbitalr*(1+eccentricity) #start at aphelion
        if isper:
            coordsep=orbitalr*(1-eccentricity)
        x0=(coordsep)*cosphi
        y0=(coordsep)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        #v= np.sqrt(masses[1]*masses[0]/masses*(2./starsep-1./(2*orbitalr)))
        vapsq=masses[1]*masses[0]/masses/orbitalr*(1-eccentricity)/(1+eccentricity)/4.
        if isper:
            vapsq=masses[1]*masses[0]/masses/orbitalr*(1+eccentricity)/(1-eccentricity)/4.
        #vapsq=masses[1]*masses[0]/masses*(1./(coordsep)-1./orbitalr)/2.
        v=np.sqrt(vapsq)
        #v= np.sqrt(masses[1]*masses[0]/masses*(1./orbitalr-2./starsep))
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)
    elif eccentricity > 1.:
        #elliptical
        orbitalr=orbitalradius #NO REDUCED MASS  (semimajor axis)
        coordsep=orbitalr*(eccentricity-1.) #start at perihelion
        isper=True
        x0=(coordsep)*cosphi
        y0=(coordsep)*sinphi
        starsep=np.sqrt((x0[0]-x0[1])**2+(y0[0]-y0[1])**2) #two stars, at opposite ends of the orbit
        Fapastron=masses[1]*masses[0]/starsep**2

        v=np.zeros(2)
        #isper:
        vapsq=masses[1]*masses[0]/masses/orbitalr*(eccentricity+1.)/(eccentricity-1.)/4. #originally e/2.
        v=np.sqrt(np.abs(vapsq))
        ux0=-v*sinphi
        uy0=v*cosphi #initial data in y only 
        uz0=np.zeros(2)

        a=np.zeros(2)
        a=Fapastron/masses
    
        ax0=-a*cosphi
        ay0=-a*sinphi
        az0=np.zeros(2)

    elif eccentricity[0]==0.0: #circular
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
        for i in np.arange(2):
            v[i]=np.sqrt(Gconstant*masses[(i+1)%2]/np.abs(r0[i]))
        print(v)
        #r0=orbitalradius #np.sqrt(x0**2+y0**2)
        ux0=-v[0]*sinphi
        uy0=v[1]*cosphi #initial data in y only 
        uz0=np.zeros(2)
        a=np.zeros(2)
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

