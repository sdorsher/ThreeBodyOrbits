import numpy as np
import math
import RK4implicit
class OrbitDiffEq:
    def __init__(self,masses,xvec,avec,t0):
        self.masses=masses
        self.xvec=xvec
        self.ti=t0
        self.avec=avec
    def dxidt(self,t,xvec):
        return xvec[:,3].transpose()
    def dyidt(self,t,xvec):
        return xvec[:,4].transpose()
    def dzidt(self,t,xvec):
        return xvec[:,5].transpose()
    def dvxidt(self,t,xvec):
        #return axi[m]
        axii=np.zeros(len(xvec[:,0]))
        #rii=np.sqrt(np.sum(xvec[:,0:3])**2)
        Gconstant=1 #6.408*10**-11
        for k in np.arange(len(xvec[:,0])):
            for j in np.arange(len(xvec[:,0])):
                if j!=k:
                    vecshift=xvec[j,:]-xvec[k,:]
                    #print(j,k,xvec[j,0],xvec[k,0],xvec[j,0]-xvec[k,0])
                    rreljk=np.sqrt(np.sum(vecshift[0:3]**2))
                    axii[j]-=Gconstant*self.masses[k]*(vecshift[0])/rreljk**3
        return axii
    def dvyidt(self,t,xvec):
        #return axi[m]
        ayii=np.zeros(len(xvec[:,0]))
        #rii=np.sqrt(np.sum(xvec[:,0:3]**2))
        Gconstant=1 #6.408*10**-11
        for k in np.arange(len(xvec[:,1])):
            for j in np.arange(len(xvec[:,1])):
                if j!=k:
                    vecshift=xvec[j,:]-xvec[k,:]
                    rreljk=np.sqrt(np.sum(vecshift[0:3]**2))
                    ayii[j]-=Gconstant*self.masses[k]*(vecshift[1])/rreljk**3
        return ayii
    def dvzidt(self,t,xvec):
        #return axi[m]
        azii=np.zeros(len(xvec[:,0]))
        #rii=np.sqrt(np.squm(xvec[:,0:3]**2))
        Gconstant=1 #6.408*10**-11
        for k in np.arange(len(xvec[:,1])):
            for j in np.arange(len(xvec[:,1])):
                if j!=k:
                    vecshift=xvec[j,:]-xvec[k,:]
                    rreljk=np.sqrt(np.sum(vecshift[0:3]**2))
                    azii[j]-=Gconstant*self.masses[k]*(vecshift[2])/rreljk**3
        return azii
    def dvecdt(self,t,xvec):
        avec=np.array([self.dvxidt(self,xvec),self.dvyidt(self,xvec),self.dvzidt(self,xvec)])
        #print("avec", avec)
        avecT=avec.transpose()
        self.avec=avecT
        dvec2=np.array([self.dxidt(t,xvec),self.dyidt(t,xvec),self.dzidt(self,xvec),avec[0,:],avec[1,:],avec[2,:]])
                       
        dvec2T=dvec2.transpose()
        return dvec2T
    def updateINTERNAL(self,xvecii,tii):
        self.xvec=xvecii
        self.ti=tii
        return self
    def update(self,xvecii,avecii,tii):
        self.xvec=xvecii
        self.avec=avecii,
        self.ti=tii
    def print2D(self):
        print(self.masses,self.xvec,self.ti)
        return self
    def list2D(self):
        return self.masses,self.xvec,self.avec,self.ti
    def timestepRK4ODE(self,step,dt):

    
        h=dt
        #tnew,ynew, intval=RK4(h,t,y,f)
        #m represents choices of mass
        i=step
        
        tnew,intvalxvec=RK4implicit.RK4implicit(h,self.ti,self.xvec,self.dvecdt)

 
        #print(xii)
        self.updateINTERNAL(intvalxvec,tnew)
        return self.masses, self.xvec,self.avec,self.ti
