#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def NewtonianForce(mass1,mass2, r):
    return mass1*mass2/r/r;

def RK4(h,t,y,f):
    k1= h*f(t,y)
    k2=h*f(t+h/2.,y+h*k1/2.)
    k3=h*f(t+h/2.,y+h*k2/2.)
    k4=h*f(t+h,y*+h*k3)
    return y+1/6.*(k1+2*k2+2*k3+k4)


#dv1dt=u1
#du1dt=Sum(F1i) excluding F11
#dv2dt=u2
#du2dt=Sum(F2i) excluding F2
#etc


def RHSU(u2):
    return u2;

def RHSF(Farr):
    return (np.sum(Farr,0)-np.trace(Farr))/2.;

def InitialData():
    random.seed(a=36);
    size1=10
    size2=50
    size3=10000
    #these are guesses from memory-- correct values will need to be filled in later or the code will need to be adapted to open or closed clusters
    masscategory0=np.ones(1);
    masscategory1=0.001*np.random.uniform(.9,1.1,size1); #Msun (jupiter)
    masscategory2=0.00001*np.random.uniform(0.2*5,size2); #Msun (Earth)
    masscategory3=0.0000001*np.random.uniform(0.01,100,size3); #comet

    #initially use an in plane orbit with random starting locations relative to the x axis
    phi0category1=np.random.uniform(0,1,size1);
    phi0category2=np.random.uniform(0,1,size2);
    phi0category2=np.random.uniform(0,1,size3);
    orbitangle1=np.zeros(size1);
    orbitangle2=np.zeros(size2);
    orbitangle3=np.zeros(size3);
    orbitalradius1=np.random.uniform(2.,50.,size1);
    orbitalradius2=np.random.uniform(.1,2,size2);
    orbitalradius3=np.random.uniform(.1,50,size3);
    eccentricity1=np.random.uniform(0.,.1,size1);
    eccentricity2=np.random.uniform(0.,.1,size2);
    eccentricity3=np.random.uniform(0,1.,size3);
    


    x00=np.zeros(1)
    y00=np.zeros(1)
    x01=orbitalradius1*np.cos(phi0category1);
    y01=orbitalradius1*np.sin(phi0category1);
    x02=orbitalradius1*np.cos(phi0category2);
    y02=orbitalradius1*np.sin(phi0category2);
    x03=orbitalradius1*np.cos(phi0category3);
    y03=orbitalradius1*np.sin(phi0category3);
    
    x0=np.zeros(1+size1+size2+size3);
    y0=np.zeros(1+size1+size2+size3);
    masses=np.zero(1+size1+size2+size3);
    x0[0]=0.0;
    x0[2:1+size1]=x01;
    x0[1+size1:1+size1+size2]=x02;
    x0[1+size1+size2:1+size1+size2+size3]=x03;
    y0[0]=0.0;
    y0[2:1+size1]=y01;
    y0[1+size1:1+size1+size2]=y02;
    y0[1+size1+size2:1+size1+size2+size3]=y03;
    masses[0]=1.0;
    masses[2:1+size1]=masscategory1;
    massess[1+size1:1+size1+size2]=masscategory2;
    masses[1+size1+size2:1+size1+size2+size3]=masscategory3;
    ecc[0]=0.0;
    ecc[2:1+size1]=eccentricity1;
    ecc[1+size1:1+size1+size2]=eccentricity2;
    ecc[1+size1+size2:1+size1+size2+size3]=eccentricity3;
    

    

    #velocity initial conditions are not trivial. 
    #I need a sun. Treat everything as a perturbation on a self consistent classical energy and momentum background. 



    


    #there is a units problem that needs to be fixed
    
    

    return masses,x0,y0, ux0, uy0;;

