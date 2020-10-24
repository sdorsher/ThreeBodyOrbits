
import math
import numpy as np

def InitialDataEqualMassConic(radius,ecc,angle,initmass):
    orbitalangle=angle
    print("angle",angle)
    phi=np.array([math.pi+orbitalangle,orbitalangle])
    orbitalradius=radius #semimajor axis
    eccentricity=ecc
    print(eccentricity)
    mass=np.ones(2)
    masses=initmass*mass #*masssun (natural units)
    return phi,orbitalangle,orbitalradius,eccentricity, masses


#rad0=50.0
#ecc0=0.9
#theta0=math.pi/6.
#mass0=1.0
#initialdataellipse=InitialDataEqualMassConic(rad0,ecc0,theta0,mass0)
#print(initialdataellipse)
